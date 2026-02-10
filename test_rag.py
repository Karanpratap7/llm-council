
import asyncio
from backend.rag import rag_engine

async def test_rag():
    conv_id = "rag-test-conv"
    
    # 1. Upload/Process file
    print("Processing file...")
    with open("secret_doc.txt", "rb") as f:
        content = f.read()
    
    result = rag_engine.process_file(conv_id, content, "secret_doc.txt")
    print(f"Process result: {result}")
    
    # 2. Search
    query = "Who is the lead of Project Omega?"
    print(f"Searching for: '{query}'")
    
    docs = rag_engine.search(conv_id, query, k=1)
    
    if docs:
        print(f"Found document chunk:")
        print(f"Source: {docs[0]['source']}")
        print(f"Score: {docs[0]['score']}")
        print(f"Text: {docs[0]['text']}")
        if "Dr. Cortex" in docs[0]['text']:
             print("✅ Success: Retrieved correct info!")
        else:
             print("❌ Failed: Did not retrieve 'Dr. Cortex'")
    else:
        print("❌ Failed: No docs found")

if __name__ == "__main__":
    asyncio.run(test_rag())
