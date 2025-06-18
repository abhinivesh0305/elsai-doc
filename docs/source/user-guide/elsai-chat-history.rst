Elsai Chat History
==================

A flexible and extensible Python package for managing chat conversation histories
with multiple storage backends and memory management strategies.

Overview
--------

The **Elsai Chat History** provides a robust solution for storing, retrieving, and managing conversational data in chat applications. It offers:

- Pluggable storage backends (JSON, SQLite, PostgreSQL, in-memory)
- Intelligent memory management strategies (summarization, trimming)
- Async support
- Multi-session tracking
- LLM-friendly interfaces

Key Features
------------

- **Multiple Storage Backends**: JSON, SQLite, PostgreSQL, in-memory
- **Memory Management**: Summarization and trimming strategies
- **Async Support**: Fully ``async/await`` compatible
- **Flexible Architecture**: Abstract base classes for easy extension
- **Session Management**: Track multiple user sessions with stats
- **LLM Integration**: Works with LangChain and other LLM tools

Prerequisites
-------------

**System Requirements**

- Python 3.13.0

Installation
------------

To install the `elsai-chat-history` package:

.. code-block:: bash

   pip install --index-url https://elsai-core-package.optisolbusiness.com/root/elsai-chat-history/ elsai-chat-history==0.1.0

Components & Usage
==================

1. Core Manager:
----------------

Basic Usage
^^^^^^^^^^^

.. code-block:: python

   import asyncio
   from elsai_chat_history.manager.chat_manager import ChatHistoryManager
   from elsai_chat_history.stores.json_store import JSONStore

   async def basic_usage():
       store = JSONStore(storage_dir="./chat_data")
       manager = ChatHistoryManager(store=store, auto_save=True)

       session_id = "user_123_session"

       await manager.add_message(session_id, role="user", content="Hello, how are you?")
       await manager.add_message(session_id, role="assistant", content="I'm good! How can I help?")

       history = await manager.get_history(session_id)
       print(f"Conversation has {len(history)} messages")

       context = await manager.get_context(session_id)
       print("Context for LLM:", context)

   asyncio.run(basic_usage())

Advanced Usage
^^^^^^^^^^^^^^

.. code-block:: python

   from elsai_chat_history.strategies.trimming import TrimmingStrategy

   async def advanced_usage():
       store = JSONStore(storage_dir="./chat_data")
       trimming = TrimmingStrategy(max_messages=50, max_tokens=4000, preserve_recent=5)

       manager = ChatHistoryManager(store=store, strategy=trimming, auto_save=True)

       await manager.add_message(
           session_id="session_123",
           role="user",
           content="What's the weather like?",
           metadata={"timestamp": "2024-01-15", "user_id": "user_456"}
       )

       stats = await manager.get_session_stats("session_123")
       print("Session stats:", stats)

   asyncio.run(advanced_usage())

2. Storage Backends
-------------------

JSON Store
^^^^^^^^^^

.. code-block:: python

   from elsai_chat_history.stores.json_store import JSONStore

   json_store = JSONStore(storage_dir="./conversations")
   manager = ChatHistoryManager(store=json_store)

SQLite Store
^^^^^^^^^^^^

.. code-block:: python

   from elsai_chat_history.stores.sqlite_store import SQLiteStore

   sqlite_store = SQLiteStore(db_path="./chat_history.db")
   manager = ChatHistoryManager(store=sqlite_store)

PostgreSQL Store
^^^^^^^^^^^^^^^^

.. code-block:: python

   from elsai_chat_history.stores.postgres_store import PostgresStore

   async def postgres_example():
       postgres_store = PostgresStore(
           connection_string="postgresql://user:password@localhost/chatdb"
       )
       manager = ChatHistoryManager(store=postgres_store)
       await manager.add_message("session_1", "user", "Hello database!")
       await postgres_store.close()

   asyncio.run(postgres_example())

Memory Store
^^^^^^^^^^^^

.. code-block:: python

   from elsai_chat_history.stores.memory_store import MemoryStore

   memory_store = MemoryStore()
   manager = ChatHistoryManager(store=memory_store)

.. note::

   Data is lost once the program ends.

3. Memory Management Strategies
-------------------------------

Trimming Strategy
^^^^^^^^^^^^^^^^^

.. code-block:: python

   from elsai_chat_history.strategies.trimming import TrimmingStrategy

   trimming = TrimmingStrategy(
       max_messages=30,
       max_tokens=3000,
       preserve_system=True,
       preserve_recent=3
   )

   manager = ChatHistoryManager(store=json_store, strategy=trimming)

Summarization Strategy
^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from elsai_chat_history.strategies.summarization import SummarizationStrategy
   
   summarization = SummarizationStrategy(
       summarizer_llm="langchain_llm_model",
       trigger_count=25,
       preserve_recent=5,
       preserve_system=True
   )

   manager = ChatHistoryManager(store=json_store, strategy=summarization)

4. Session Management
---------------------

.. code-block:: python

   # List sessions
   sessions = await manager.list_sessions()
   print("Active sessions:", sessions)

   # Clear a session
   await manager.clear_session("session_to_delete")

   # Manually save session
   await manager.save_session("session_123")

   # Get session statistics
   stats = await manager.get_session_stats("session_123")
   print(f"Total messages: {stats['total_messages']}")
   print(f"Role distribution: {stats['role_distribution']}")

