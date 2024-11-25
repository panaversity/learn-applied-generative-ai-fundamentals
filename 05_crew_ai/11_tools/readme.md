# Tools

In CrewAI, [tools](https://docs.crewai.com/concepts/tools) are specialized functions or capabilities that agents utilize to perform various tasks, such as web searching, data analysis, content generation, and agent collaboration. These tools enhance agents' abilities by integrating specific functionalities into their workflows. 

**Creating Custom Tools in CrewAI**

You can create custom tools in CrewAI through two primary methods:

1. **Subclassing `BaseTool`**: This approach involves defining a new class that inherits from `BaseTool`, specifying attributes like `name`, `description`, and implementing the `_run` method for the tool's operational logic.

   ```python
   from crewai_tools import BaseTool

   class MyCustomTool(BaseTool):
       name: str = "Name of my tool"
       description: str = "Clear description for what this tool is useful for; your agent will need this information to use it."

       def _run(self, argument: str) -> str:
           # Implementation goes here
           pass
   ```

2. **Using the `@tool` Decorator**: For a more straightforward approach, you can use the `@tool` decorator to transform a function into a tool with minimal overhead.

   ```python
   from crewai_tools import tool

   @tool("Name of my tool")
   def my_tool(question: str) -> str:
       """Clear description for what this tool is useful for; your agent will need this information to use it."""
       # Function logic here
       pass
   ```

Both methods allow you to define custom functionalities that agents can invoke as needed. 

**Function Calling in CrewAI**

Function calling in CrewAI refers to the mechanism by which agents invoke these tools to perform specific actions. By defining custom tools, you enable agents to execute tailored functions, thereby enhancing their problem-solving capabilities. This process involves creating tools that agents can call upon during their operations, effectively allowing them to perform complex tasks autonomously. 

By integrating custom tools and utilizing function calling, you can significantly expand the capabilities of your CrewAI agents, enabling them to handle a broader range of tasks with greater efficiency. 

## Calculator Custom Tool Example

To integrate a custom calculator tool into CrewAI using both subclassing and the `@tool` decorator, and to incorporate the latest Flows functionality, follow the steps below.

**1. Subclassing `BaseTool`**

First, define a custom calculator tool by subclassing `BaseTool`:

```python
from crewai_tools import BaseTool

class CalculatorTool(BaseTool):
    name: str = "Calculator"
    description: str = "Performs basic arithmetic operations: addition, subtraction, multiplication, and division."

    def _run(self, expression: str) -> str:
        """
        Evaluates a basic arithmetic expression.
        Args:
            expression (str): A string containing the arithmetic expression to evaluate.
        Returns:
            str: The result of the arithmetic operation.
        """
        try:
            # Evaluate the arithmetic expression safely
            result = eval(expression, {"__builtins__": None}, {})
            return str(result)
        except Exception as e:
            return f"Error evaluating expression: {e}"
```

**2. Using the `@tool` Decorator**

Alternatively, create the calculator tool using the `@tool` decorator:

```python
from crewai_tools import tool

@tool("Calculator")
def calculator_tool(expression: str) -> str:
    """
    Evaluates a basic arithmetic expression.
    Args:
        expression (str): A string containing the arithmetic expression to evaluate.
    Returns:
        str: The result of the arithmetic operation.
        """
    try:
        # Evaluate the arithmetic expression safely
        result = eval(expression, {"__builtins__": None}, {})
        return str(result)
    except Exception as e:
        return f"Error evaluating expression: {e}"
```

**3. Integrating with CrewAI Flows**

To utilize the custom calculator tool within a CrewAI Flow, follow these steps:

- **Define an Agent**: Create an agent that will use the calculator tool.

  ```python
  from crewai import Agent

  calculator_agent = Agent(
      role="Calculator Agent",
      goal="Solve arithmetic expressions provided by the user.",
      tools=[CalculatorTool()],  # or [calculator_tool] if using the decorator approach
      verbose=True
  )
  ```

- **Define a Task**: Create a task that specifies the agent's objective.

  ```python
  from crewai import Task

  calculation_task = Task(
      name="CalculationTask",
      description="Evaluate the arithmetic expression provided by the user.",
      expected_output="The result of the arithmetic operation.",
      agent=calculator_agent
  )
  ```

- **Define a Flow**: Implement a Flow that orchestrates the task execution.

  ```python
  from crewai.flow.flow import Flow, start
  from pydantic import BaseModel

  class CalculationState(BaseModel):
      expression: str = ""
      result: str = ""

  class CalculatorFlow(Flow[CalculationState]):
      @start()
      def get_expression(self):
          # In a real scenario, replace input() with appropriate input handling
          expression = input("Enter an arithmetic expression: ")
          self.state.expression = expression
          return expression

      @listen(get_expression)
      def perform_calculation(self, expression):
          # Use the calculator tool to evaluate the expression
          result = calculator_agent.tools[0]._run(expression)
          self.state.result = result
          return result

      @listen(perform_calculation)
      def display_result(self, result):
          print(f"The result of the expression is: {result}")
  ```

- **Execute the Flow**: Run the Flow to perform the calculation.

  ```python
  if __name__ == "__main__":
      flow = CalculatorFlow()
      flow.kickoff()
  ```

**Important Considerations:**

- **Security**: The `eval` function can execute arbitrary code, which poses security risks. In a production environment, implement strict validation and sanitization of the input expression to prevent code injection vulnerabilities.

- **Functionality**: These examples handle basic arithmetic operations. For more complex calculations or additional functionalities, consider integrating with specialized libraries or APIs.

By following these steps, you can create a custom calculator tool and integrate it into a CrewAI Flow, enabling agents to perform arithmetic operations within a structured workflow. 


## Pre-Built Tools

CrewAI offers a comprehensive suite of [pre-built tools](https://docs.crewai.com/concepts/tools#available-crewai-tools) designed to enhance the capabilities of AI agents across various tasks. Below is a categorized list of these tools:

**File Operations:**
- **FileWriterTool:** Enables agents to write data to files.
- **FileReadTool:** Allows agents to read and process data from files.
- **DirectoryReadTool:** Facilitates reading and processing of directory structures and their contents.

**Web Scraping:**
- **ScrapeWebsiteTool:** Enables agents to scrape entire websites for comprehensive data collection.
- **SeleniumScrapingTool:** Utilizes Selenium for dynamic web scraping tasks.
- **ScrapeElementFromWebsiteTool:** Allows scraping of specific elements from websites for targeted data extraction.

**Database Interactions:**
- **PGSearchTool:** Optimized for searching within PostgreSQL databases, suitable for database queries.
- **MySQLSearchTool:** Designed for interactions with MySQL databases.

**API Integrations:**
- **SerperApiTool:** Integrates with the Serper API for enhanced search capabilities.
- **EXASearchTool:** Performs exhaustive searches across various data sources.

**AI-Powered Tools:**
- **DallETool:** Generates images using the DALL-E API.
- **VisionTool:** Provides image generation capabilities, similar to DallETool.

**Document Search and Analysis:**
- **PDFSearchTool:** Aimed at searching within PDF documents, ideal for processing scanned documents.
- **DOCXSearchTool:** Tailored for searching within DOCX files, useful for processing Word documents.
- **TXTSearchTool:** Focused on searching within text (.txt) files, suitable for unstructured data.
- **CSVSearchTool:** Designed for searching within CSV files, tailored to handle structured data.
- **JSONSearchTool:** Optimized for searching within JSON files, catering to structured data handling.
- **XMLSearchTool:** Designed for searching within XML files, suitable for structured data formats.
- **MDXSearchTool:** Tailored for searching within Markdown (MDX) files, useful for documentation.

**Web Interaction and Search:**
- **WebsiteSearchTool:** A RAG (Retrieval-Augmented Generation) tool for searching website content, optimized for web data extraction.
- **FirecrawlSearchTool:** Searches webpages using Firecrawl and returns the results.
- **FirecrawlCrawlWebsiteTool:** Crawls webpages using Firecrawl.
- **FirecrawlScrapeWebsiteTool:** Scrapes webpages using Firecrawl and returns their contents.

**Code and Development:**
- **CodeDocsSearchTool:** A RAG tool optimized for searching through code documentation and related technical documents.
- **CodeInterpreterTool:** Interprets Python code, facilitating code execution and analysis.

**Media and Content:**
- **YoutubeChannelSearchTool:** A RAG tool for searching within YouTube channels, useful for video content analysis.
- **YoutubeVideoSearchTool:** Aimed at searching within YouTube videos, ideal for video data extraction.

**Miscellaneous:**
- **BrowserbaseLoadTool:** Interacts with and extracts data from web browsers.
- **ComposioTool:** Enables the use of Composio tools.
- **LlamaIndexTool:** Facilitates the use of LlamaIndex tools.
- **RagTool:** A general-purpose RAG tool capable of handling various data sources and types.

These tools are designed to be easily integrated into your AI workflows, enhancing the functionality and efficiency of your CrewAI agents. For detailed documentation and

CrewAI provides a variety of prebuilt tools that empower AI agents to handle tasks such as file operations, web scraping, database interactions, API integration, document search, and media analysis. For a detailed and official list, checking CrewAI's documentation or resources directly would be ideal. 