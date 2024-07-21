# AWS CodeBuild Setup

## Steps

1. **Create a CodeBuild Project**:
    - Go to the AWS CodeBuild console and click "Create build project".
    - Provide a project name (e.g., `DataEngineeringBuildProject`).

2. **Source**:
    - Select the source provider (e.g., GitHub) and connect to your repository.

3. **Environment**:
    - Select the environment image (e.g., `aws/codebuild/standard:4.0`).
    - Choose the operating system, runtime, and image version.
    - Set up environment variables if needed.

4. **Buildspec**:
    - Use the buildspec file located in your repository (e.g., `buildspec.yml`).

5. **Artifacts**:
    - Configure the artifacts to be stored in an S3 bucket.

6. **Review and Create**:
    - Review your build project configuration and click "Create build project".

### Example Buildspec File

- `buildspec.yml`

```yaml
version: 0.2

phases:
  install:
    commands:
      - echo Installing dependencies...
      - pip install -r requirements.txt
  pre_build:
    commands:
      - echo Running pre-build tasks...
  build:
    commands:
      - echo Building the project...
      - python setup.py build
  post_build:
    commands:
      - echo Running post-build tasks...
      - python setup.py test

artifacts:
  files:
    - '**/*'
  discard-paths: yes
