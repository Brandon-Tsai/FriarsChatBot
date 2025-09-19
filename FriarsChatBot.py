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
    model="gpt-4.1-2025-04-14"   # or another supported base model
)

print("Job ID:", job.id)
