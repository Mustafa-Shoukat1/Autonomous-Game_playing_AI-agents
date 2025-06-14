"""
AI 3D PyGame Visualizer with DeepSeek R1
----------------------------------------
This application demonstrates the capabilities of large language models for code generation
and browser automation in creating interactive PyGame simulations.

Key features:
- Natural language to PyGame code generation using DeepSeek Reasoner for code logic
- Code cleanup and optimization using OpenAI's GPT models
- Automated visualization on Trinket.io using browser automation
- Web-based interface using Streamlit for easy interaction

The system works through a pipeline of specialized AI agents:
1. Code generation agent (using DeepSeek)
2. Code extraction and cleaning agent (using OpenAI)
3. Browser automation agents (for code execution on Trinket.io)
"""

import streamlit as st
from openai import OpenAI
from agno.agent import Agent as AgnoAgent
from agno.models.openai import OpenAIChat as AgnoOpenAIChat
from langchain_openai import ChatOpenAI 
import asyncio
from browser_use import Browser

# Configure the Streamlit page with wide layout for better visualization
st.set_page_config(page_title="PyGame Code Generator", layout="wide")

# Initialize session state for persistence across page reloads
if "api_keys" not in st.session_state:
    st.session_state.api_keys = {
        "deepseek": "",  # API key for DeepSeek Reasoner
        "openai": ""     # API key for OpenAI code extraction
    }

# Streamlit sidebar for API keys configuration
with st.sidebar:
    st.title("API Keys Configuration")
    st.session_state.api_keys["deepseek"] = st.text_input(
        "DeepSeek API Key",
        type="password",
        value=st.session_state.api_keys["deepseek"]
    )
    st.session_state.api_keys["openai"] = st.text_input(
        "OpenAI API Key",
        type="password",
        value=st.session_state.api_keys["openai"]
    )
    
    st.markdown("---")
    st.info("""
    📝 How to use:
    1. Enter your API keys above
    2. Write your PyGame visualization query
    3. Click 'Generate Code' to get the code
    4. Click 'Generate Visualization' to:
       - Open Trinket.io PyGame editor
       - Copy and paste the generated code
       - Watch it run automatically
    """)

# Main UI components
st.title("🎮 AI 3D Visualizer with DeepSeek R1")
example_query = "Create a particle system simulation where 100 particles emit from the mouse position and respond to keyboard-controlled wind forces"
query = st.text_area(
    "Enter your PyGame query:",
    height=70,
    placeholder=f"e.g.: {example_query}"
)

# Split the buttons into columns for better layout
col1, col2 = st.columns(2)
generate_code_btn = col1.button("Generate Code")
generate_vis_btn = col2.button("Generate Visualization")

# Code generation logic
if generate_code_btn and query:
    # Check for API keys
    if not st.session_state.api_keys["deepseek"] or not st.session_state.api_keys["openai"]:
        st.error("Please provide both API keys in the sidebar")
        st.stop()

    # Initialize Deepseek client for code generation
    deepseek_client = OpenAI(
        api_key=st.session_state.api_keys["deepseek"],
        base_url="https://api.deepseek.com"
    )

    # System prompt for Deepseek Reasoner
    system_prompt = """You are a Pygame and Python Expert that specializes in making games and visualisation through pygame and python programming. 
    During your reasoning and thinking, include clear, concise, and well-formatted Python code in your reasoning. 
    Always include explanations for the code you provide."""

    try:
        # Get reasoning from Deepseek
        with st.spinner("Generating solution..."):
            deepseek_response = deepseek_client.chat.completions.create(
                model="deepseek-reasoner",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": query}
                ],
                max_tokens=1  
            )

        # Extract and display reasoning from Deepseek
        reasoning_content = deepseek_response.choices[0].message.reasoning_content
        print("\nDeepseek Reasoning:\n", reasoning_content)
        with st.expander("R1's Reasoning"):      
            st.write(reasoning_content)

        # Initialize Claude agent (using PhiAgent) for code extraction
        openai_agent = AgnoAgent(
            model=AgnoOpenAIChat(
                id="gpt-4o",
                api_key=st.session_state.api_keys["openai"]
            ),
            show_tool_calls=True,
            markdown=True
        )

        # Extract code from reasoning content
        extraction_prompt = f"""Extract ONLY the Python code from the following content which is reasoning of a particular query to make a pygame script. 
        Return nothing but the raw code without any explanations, or markdown backticks:
        {reasoning_content}"""

        with st.spinner("Extracting code..."):
            code_response = openai_agent.run(extraction_prompt)
            extracted_code = code_response.content

        # Store the generated code in session state for later use
        st.session_state.generated_code = extracted_code
        
        # Display the extracted code in a collapsible section
        with st.expander("Generated PyGame Code", expanded=True):      
            st.code(extracted_code, language="python")
            
        st.success("Code generated successfully! Click 'Generate Visualization' to run it.")

    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

# Visualization generation logic
elif generate_vis_btn:
    if "generated_code" not in st.session_state:
        st.warning("Please generate code first before visualization")
    else:
        # Asynchronous function to run PyGame code on Trinket.io using browser automation
        async def run_pygame_on_trinket(code: str) -> None:
            browser = Browser()
            from browser_use import Agent 
            async with await browser.new_context() as context:
                model = ChatOpenAI(
                    model="gpt-4o", 
                    api_key=st.session_state.api_keys["openai"]
                )
                
                # Define the AI agents for browser automation
                agent1 = Agent(
                    task='Go to https://trinket.io/features/pygame, thats your only job.',
                    llm=model,
                    browser_context=context,
                )
                
                executor = Agent(
                    task='Executor. Execute the code written by the User by clicking on the run button on the right. ',
                    llm=model,
                    browser_context=context
                )

                coder = Agent(
                    task='Coder. Your job is to wait for the user for 10 seconds to write the code in the code editor.',
                    llm=model,
                    browser_context=context
                )
                
                viewer = Agent(
                    task='Viewer. Your job is to just view the pygame window for 10 seconds.',
                    llm=model,
                    browser_context=context,
                )

                # Run the defined agents in sequence to automate the entire process
                with st.spinner("Running code on Trinket..."):
                    try:
                        await agent1.run()
                        await coder.run()
                        await executor.run()
                        await viewer.run()
                        st.success("Code is running on Trinket!")
                    except Exception as e:
                        st.error(f"Error running code on Trinket: {str(e)}")
                        st.info("You can still copy the code above and run it manually on Trinket")

        # Run the async function with the stored code
        asyncio.run(run_pygame_on_trinket(st.session_state.generated_code))

# Warning for empty query
elif generate_code_btn and not query:
    st.warning("Please enter a query before generating code")