from nemoguardrails import LLMRails, RailsConfig

# Load a guardrails configuration from the specified path.
config = RailsConfig.from_path("./config")
rails = LLMRails(config)

# greeting
msg = {
    "role": "user",
    "content": "Hello!"
}

# # insult
# msg = {
#     "role": "user",
#     "content": "You are total crap!"
# }

completion = rails.generate(
    messages=[msg]
)

print(completion)
