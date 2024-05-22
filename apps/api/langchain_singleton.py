from decouple import config
from langchain.agents import create_sql_agent
from langchain.agents.agent_types import AgentType
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
from langchain_community.chat_models import ChatOpenAI
from langchain_community.utilities import SQLDatabase


class LangChainAgentSingleton:
    _instance = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            database_uri = config('DATABASE_URL')
            api_key = config('OPENAI_API_KEY')
            model_name = config('OPENAI_MODEL_NAME', default='gpt-3.5-turbo')

            if not database_uri.startswith('sqlite:///'):
                database_uri = f'sqlite:///{database_uri}'

            my_db = SQLDatabase.from_uri(database_uri)
            my_llm = ChatOpenAI(model_name=model_name, openai_api_key=api_key)

            cls._instance = create_sql_agent(
                llm=my_llm,
                toolkit=SQLDatabaseToolkit(db=my_db, llm=my_llm),
                agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
                handle_parsing_errors=True,
                verbose=True,
                return_intermediate_steps=True
            )
        return cls._instance
