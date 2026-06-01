from agents import build_search_agent, build_reader_agent, writer_chain, critic_chain

def run_research_pipeline(topic: str) -> dict:

    state = {}

    # search agent working
    print("\n "+" ="*50)
    print("Step 1 - search agent is working...")
    print("="*50)

    search_agent = build_search_agent()
    search_result = search_agent.invoke({
    "messages": [("user",
        f"Search for information about: {topic}\n\n"
        f"IMPORTANT INSTRUCTIONS:\n"
        f"- Use the web_search tool\n"
        f"- Return the COMPLETE raw output from the tool\n"
        f"- Do NOT summarize anything\n"
        f"- Keep ALL URLs exactly as returned\n"
        f"- List every result with Title, URL and Snippet"
    )]
})

    state["search_result"] = search_result['messages'][-1].content

    print("\n search result ",state['search_result'])


    #  step 2 - reader agent working
    print("\n "+" ="*50)
    print("Step 2 - reader agent is scraping top results...")
    print("="*50)

    reader_agent = build_reader_agent()
    reader_result = reader_agent.invoke({
    "messages": [("user",
        f"From the search results below, extract the URLs and scrape "
        f"the MOST relevant one using the scrape_url tool.\n\n"
        f"Search Results:\n{state['search_result'][:800]}\n\n"
        f"Steps:\n"
        f"1. Find all lines starting with 'URL :'\n"
        f"2. Pick the most relevant URL for the topic: '{topic}'\n"
        f"3. Call scrape_url with that URL\n"
        f"4. Return the scraped content"
    )]
})

    state['scraped_content'] = reader_result['messages'][-1].content

    print("\n scraped content ",state['scraped_content'])

    # step 3 - writer chain working
    print("\n "+" ="*50)
    print("Step 3 - writer chain is generating the research report...")
    print("="*50)
    research_combined = (
        f"SEARCH RESULTS:\n{state['search_result']}\n\n"
        f"SCRAPED CONTENT:\n{state['scraped_content']}"
    )
    state["report"] = writer_chain.invoke({
        "topic": topic,
        "research": research_combined
    })

    print("\n Final Research Report:\n",state['report'])

    # step 4 - critic chain working
    print("\n "+" ="*50)
    print("Step 4 - critic chain is evaluating the report...")
    print("="*50)
    state["feedback"] =critic_chain.invoke({
        "report": state['report']
    })

    print("\n Critic Feedback:\n",state['feedback'])

    return state

if __name__ == "__main__":
    topic = input("Enter a research topic: ")
    run_research_pipeline(topic)