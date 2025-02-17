import subprocess
command = [
    "aws", "codebuild", "create-project",
    "--name", "my-app-build",
    "--source", "type=GITHUB,location=https://github.com/NateChris14/ML-ENDTOEND",
    "--artifacts", "type=NO_ARTIFACTS",
    "--environment", "type=LINUX_CONTAINER,image=aws/codebuild/python:3.9,computeType=BUILD_GENERAL1_SMALL",
    "--service-role", "arn:aws:iam::145023104239:role/CodeBuildServiceRole",
    "--timeout-in-minutes", "30",
    "--tags", "key=Project,value=FlaskApp"
]
subprocess.run(command)
