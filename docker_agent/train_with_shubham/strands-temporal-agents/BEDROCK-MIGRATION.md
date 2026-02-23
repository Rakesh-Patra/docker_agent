# Migration from Ollama to AWS Bedrock

This document explains the migration from Ollama to AWS Bedrock for the Strands Temporal Agents project.

## What Changed

The project now uses **AWS Bedrock** with Claude models instead of local Ollama for AI inference. This provides:

- **Managed Service**: No need to run local LLM infrastructure
- **Enterprise-Grade**: Production-ready with AWS SLAs
- **Latest Models**: Access to Claude Sonnet 4 and other foundation models
- **Scalability**: Automatic scaling without local resource constraints

## Prerequisites

### 1. AWS Account Setup

You need an AWS account with access to Amazon Bedrock:

1. Sign in to the [AWS Management Console](https://console.aws.amazon.com/)
2. Navigate to Amazon Bedrock
3. Request model access (see below)

### 2. Request Bedrock Model Access

Before using Claude models, request access:

1. Open the [Amazon Bedrock console](https://console.aws.amazon.com/bedrock/)
2. In the navigation pane, choose **Model access**
3. Choose **Manage model access**
4. Select **Anthropic - Claude Sonnet 4**
5. Review terms and choose **Request model access**

Access is typically granted immediately.

### 3. Configure AWS Credentials

Choose one of these methods:

**Option A: AWS CLI (Recommended)**
```bash
aws configure
```

**Option B: Environment Variables**
```bash
export AWS_ACCESS_KEY_ID=your_access_key
export AWS_SECRET_ACCESS_KEY=your_secret_key
export AWS_REGION=us-east-1
```

**Option C: IAM Role** (when running on AWS infrastructure)
- Attach an IAM role with Bedrock permissions to your EC2 instance or Lambda function

### 4. IAM Permissions

Your IAM user or role needs these permissions:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "bedrock:InvokeModel",
        "bedrock:InvokeModelWithResponseStream"
      ],
      "Resource": "*"
    }
  ]
}
```

For production, scope the `Resource` to specific model ARNs.

## Installation

### 1. Update Dependencies

```bash
pip install -r requirements.txt
```

This now includes `boto3>=1.34.0` for AWS SDK support.

### 2. Configure Environment (Optional)

Copy and customize the environment file:

```bash
cp .env.example .env
```

Edit `.env` to set your preferences:

```bash
# AWS Bedrock Configuration
AWS_REGION=us-east-1
BEDROCK_MODEL_ID=us.anthropic.claude-sonnet-4-20250514-v1:0
```

## Configuration Options

### Model Selection

The default model is Claude Sonnet 4 with cross-region inference:

```python
BEDROCK_MODEL_ID = "us.anthropic.claude-sonnet-4-20250514-v1:0"
```

**For regions supporting inference profiles** (us-east-1, us-west-2, etc.):
- Use: `us.anthropic.claude-sonnet-4-20250514-v1:0`

**For regions without inference profiles**:
- Use: `anthropic.claude-sonnet-4-20250514-v1:0`

See [Amazon Bedrock documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/inference-profiles.html) for details.

### Region Selection

Set your preferred AWS region:

```bash
export AWS_REGION=us-east-1  # or us-west-2, eu-west-1, etc.
```

Available regions: us-east-1, us-west-2, eu-west-1, eu-central-1, ap-southeast-1, ap-northeast-1

## Usage

### Simple Agent

```bash
python agent.py
```

The agent now uses Bedrock automatically. No code changes needed!

### Temporal Agent

```bash
# Terminal 1: Start Temporal server
temporal server start-dev

# Terminal 2: Start worker
python worker.py

# Terminal 3: Run client
python client.py
```

### Docker Monitor

```bash
cd docker_monitor
python docker_agent.py
```

## Verification

### Test AWS Credentials

```bash
aws sts get-caller-identity
```

### Test Bedrock Access

```bash
aws bedrock list-foundation-models --region us-east-1
```

### Test Agent

```bash
python agent.py
# Try: "What time is it?"
```

## Troubleshooting

### Model Access Error

**Error**: `You don't have access to the model with the specified model ID`

**Solution**: Request model access in the Bedrock console (see Prerequisites above)

### Inference Profile Error

**Error**: `Invocation of model ID with on-demand throughput isn't supported`

**Solution**: Your region doesn't support inference profiles. Change model ID:
- From: `us.anthropic.claude-sonnet-4-20250514-v1:0`
- To: `anthropic.claude-sonnet-4-20250514-v1:0`

### Invalid Model Identifier

**Error**: `The provided model identifier is invalid`

**Solution**: You're using an inference profile model ID in a region that doesn't support them. Use the base model ID instead.

### Credentials Not Found

**Error**: `Unable to locate credentials`

**Solution**: Configure AWS credentials using `aws configure` or environment variables

### Region Not Supported

**Error**: `Could not connect to the endpoint URL`

**Solution**: Bedrock is not available in your region. Use a supported region like us-east-1

## Cost Considerations

AWS Bedrock charges per token:
- **Input tokens**: ~$0.003 per 1K tokens
- **Output tokens**: ~$0.015 per 1K tokens

Typical agent query costs $0.001-0.01 depending on complexity.

See [Amazon Bedrock pricing](https://aws.amazon.com/bedrock/pricing/) for current rates.

## Comparison: Ollama vs Bedrock

| Feature | Ollama | AWS Bedrock |
|---------|--------|-------------|
| **Setup** | Install locally | AWS account + credentials |
| **Cost** | Free (local compute) | Pay per token |
| **Latency** | Low (local) | Higher (network) |
| **Scalability** | Limited by hardware | Unlimited |
| **Maintenance** | Manual updates | Fully managed |
| **Models** | Open source | Claude, Titan, Jurassic |
| **Production** | Not recommended | Enterprise-ready |

## Migration Checklist

- [ ] AWS account created
- [ ] Bedrock model access requested and granted
- [ ] AWS credentials configured
- [ ] IAM permissions verified
- [ ] Dependencies updated (`pip install -r requirements.txt`)
- [ ] Environment variables configured (optional)
- [ ] Simple agent tested
- [ ] Temporal agent tested
- [ ] Docker monitor tested

## Rollback (If Needed)

To revert to Ollama:

1. Install Ollama: https://ollama.ai/
2. Pull model: `ollama pull llama3.2:latest`
3. Revert code changes (use git)
4. Update config.py to use OllamaModel

## Additional Resources

- [Strands Agents Bedrock Documentation](https://strandsagents.com/latest/documentation/docs/user-guide/concepts/model-providers/amazon-bedrock/)
- [Amazon Bedrock User Guide](https://docs.aws.amazon.com/bedrock/latest/userguide/)
- [AWS CLI Configuration](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html)
- [IAM Permissions for Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/security-iam.html)

## Support

For issues:
1. Check troubleshooting section above
2. Verify AWS credentials and permissions
3. Check Bedrock service status
4. Review CloudWatch logs for detailed errors
