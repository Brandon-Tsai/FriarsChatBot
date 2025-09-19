from openai import OpenAI
client = OpenAI()

# Upload file
file = client.files.create(
    file=open("training_data.jsonl", "rb"),
    purpose="fine-tune"
)

# Create fine-tune job
job = client.fine_tuning.jobs.create(
    training_file=file.id,
    model="gpt-3.5-turbo"   # or another supported base model
)

print("Job ID:", job.id)
