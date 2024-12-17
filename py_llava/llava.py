import ollama

res = ollama.chat(
	model="llava",
	messages=[
		{
			'role': 'user',
			'content': 'Describe this image:',
			'images': ['./dancing.jpg']
		}
	]
)

print(res['message']['content'])