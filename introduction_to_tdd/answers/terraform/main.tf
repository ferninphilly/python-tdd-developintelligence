provider "aws" {
  region = "us-east-1"
  profile="codices"
  version = "~> 2.24"
}

variable "function_name" {
  default = "test_movie_function"
}

variable "handler" {
  default = "badmoviesapi.handler"
}

variable "runtime" {
  default = "python3.6"
}


resource "aws_lambda_function" "practice_lambda_function" {
  role             = aws_iam_role.lambda_exec_role.arn
  handler          = var.handler
  runtime          = var.runtime
  filename         = "../badmoviesapi/badmoviesapi.zip"
  function_name    = var.function_name
  source_code_hash = base64sha256("../badmoviesapi/badmoviesapi.zip")
  environment {
    variables = {
      API_URL = "http://www.omdbapi.com/"
      API_KEY = "apikey=dd070ac3"
      ENV = "prod"
    }
  }
}

resource "aws_iam_role" "lambda_exec_role" {
  name        = "lambda_exec"
  path        = "/"
  description = "Allows Lambda Function to call AWS services on your behalf."

  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
EOF
}

resource "aws_api_gateway_rest_api" "test_badmovies" {
  name        = "BadmoviesAPI"
  description = "Our bad movies gateway"
}

resource "aws_api_gateway_resource" "movie" {
  rest_api_id = aws_api_gateway_rest_api.test_badmovies.id
  parent_id   = aws_api_gateway_rest_api.test_badmovies.root_resource_id
  path_part   = "movie"
}

resource "aws_api_gateway_method" "movie" {
  rest_api_id   = aws_api_gateway_rest_api.test_badmovies.id
  resource_id   = aws_api_gateway_resource.movie.id
  http_method   = "ANY"
  authorization = "NONE"
}

resource "aws_api_gateway_integration" "lambda" {
  rest_api_id = aws_api_gateway_rest_api.test_badmovies.id
  resource_id = aws_api_gateway_method.movie.resource_id
  http_method = aws_api_gateway_method.movie.http_method

  integration_http_method = "POST"
  type                    = "AWS_PROXY"
  uri                     = aws_lambda_function.practice_lambda_function.invoke_arn
}

 resource "aws_api_gateway_deployment" "test-lambda" {
  depends_on = [
    "aws_api_gateway_integration.lambda"
  ]

  rest_api_id = aws_api_gateway_rest_api.test_badmovies.id
  stage_name  = "test"
}

resource "aws_lambda_permission" "apigw" {
  statement_id  = "AllowAPIGatewayInvoke"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.practice_lambda_function.arn
  principal     = "apigateway.amazonaws.com"

  source_arn = "${aws_api_gateway_deployment.test-lambda.execution_arn}/*/*"
}


# See also the following AWS managed policy: AWSLambdaBasicExecutionRole
resource "aws_iam_policy" "lambda_logging" {
  name = "lambda_logging_4"
  path = "/"
  description = "IAM policy for logging from a lambda"

  policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": [
        "logs:CreateLogGroup",
        "logs:CreateLogStream",
        "logs:PutLogEvents"
      ],
      "Resource": "arn:aws:logs:*:*:*",
      "Effect": "Allow"
    }
  ]
}
EOF
}

resource "aws_iam_role_policy_attachment" "lambda_logs" {
  role = aws_iam_role.lambda_exec_role.name
  policy_arn = aws_iam_policy.lambda_logging.arn
}

 output "dev_url" {
  value = aws_api_gateway_deployment.test-lambda.invoke_url
}