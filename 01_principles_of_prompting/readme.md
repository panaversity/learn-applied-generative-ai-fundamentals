# Five Core Principles of Prompting

There are five core principles of prompting for generative AI: Give Direction, Specify Format, Provide Examples, Evaluate Quality, and Divide Labor. While not a perfect system, these five principles can be applied to get better and more reliable outputs from AI. 

### The Five Principles of Prompting
*   **Give Direction** focuses on the style of the response. For example, you could ask for product names "in the style of Steve Jobs". You can also give the AI the context a human might need to respond to the prompt, like including a set of rules for naming products.
*   **Specify Format** focuses on the type of output you want, like a JSON file or a stock photo. When style and format clash, it is usually best to drop whichever one is less important to the final output. 
*   **Provide Examples** can involve giving examples of the task done well. In image generation, this usually means providing a base image, also called "img2img". Providing examples can increase the length of the prompt and therefore increase costs if you are using a paid API. 
*   **Evaluate Quality** can be as simple as a thumbs up/thumbs down rating system or as complex as comparing different models against each other to measure performance. When evaluating the quality of a prompt it's important to consider if any instructions are unnecessary or even degrading the quality of the output.
*   **Divide Labor** means breaking up the task into smaller parts to be solved individually and then aggregated together. This can help make AI tools more efficient by allowing them to focus on specific aspects of a problem. 

These five principles can be implemented across a number of generative AI tasks and models. Before using the output of generative AI, you should always review it to make sure that it is clear, relevant, and accurate.  Generative AI should be used to help humans, but the final output is always up to the human. 

### Example

You are a Google Cloud program manager. Draft an executive summary email to [persona] based on
[details about relevant program docs]. Limit to bullet points.
