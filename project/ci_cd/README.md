# CI/CD Configuration

## AWS CodePipeline

### Steps to Set Up

1. **Create a CodePipeline**:
    - Go to the AWS CodePipeline console and click "Create pipeline".
    - Provide a pipeline name (e.g., `DataEngineeringPipeline`).

2. **Source Stage**:
    - Select "Source provider" as GitHub.
    - Connect to your GitHub repository and select the repository and branch to use as the source.

3. **Build Stage**:
    - Select "Build provider" as AWS CodeBuild.
    - Create a new build project if you don't have one already.

4. **Deploy Stage** (optional):
    - If you have deployment steps, configure them here. This can include Lambda deployment, ECS deployment, etc.

5. **Review and Create**:
    - Review your pipeline configuration and click "Create pipeline".

### Configuration File

- `pipeline_configuration.json`

```json
{
  "pipeline": {
    "name": "DataEngineeringPipeline",
    "roleArn": "arn:aws:iam::your-account-id:role/service-role/AWSCodePipelineServiceRole",
    "artifactStore": {
      "type": "S3",
      "location": "codepipeline-artifacts-bucket"
    },
    "stages": [
      {
        "name": "Source",
        "actions": [
          {
            "name": "SourceAction",
            "actionTypeId": {
              "category": "Source",
              "owner": "ThirdParty",
              "provider": "GitHub",
              "version": "1"
            },
            "configuration": {
              "Owner": "your-github-username",
              "Repo": "your-repo-name",
              "Branch": "main",
              "OAuthToken": "your-oauth-token"
            },
            "outputArtifacts": [
              {
                "name": "SourceOutput"
              }
            ]
          }
        ]
      },
      {
        "name": "Build",
        "actions": [
          {
            "name": "BuildAction",
            "actionTypeId": {
              "category": "Build",
              "owner": "AWS",
              "provider": "CodeBuild",
              "version": "1"
            },
            "configuration": {
              "ProjectName": "DataEngineeringBuildProject"
            },
            "inputArtifacts": [
              {
                "name": "SourceOutput"
              }
            ],
            "outputArtifacts": [
              {
                "name": "BuildOutput"
              }
            ]
          }
        ]
      }
    ]
  }
}
