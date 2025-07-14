# MCP Version - System Architecture Flow

## Interactive Flowchart

```mermaid
graph TD
    %% User Interface Layer
    A[User Input: Natural Language] --> B[Streamlit Frontend]
    B --> C[OpenAI GPT-4o-mini]
    
    %% AI Processing
    C --> D{AI Decision}
    D -->|Function Call Needed| E[Function Selection]
    D -->|Direct Response| F[Text Response]
    
    %% Function Mapping
    E --> G[Tool Registry]
    G --> H{Function Type}
    
    %% File Operations Branch
    H -->|File Operations| I[Files MCP Server<br/>:8002]
    I --> J[FileOperations Class]
    J --> K[Shared Files Directory]
    
    %% Random Facts Branch
    H -->|Random Facts| L[API MCP Server<br/>:8001]
    L --> M[RandomFacts Class]
    
    %% Results Flow
    K --> N[File Result]
    M --> O[Random Fact Result]
    N --> P[HTTP Response]
    O --> P
    P --> Q[Streamlit Display]
    F --> Q
    
    %% Styling
    classDef userLayer fill:#e1f5fe,stroke:#01579b,stroke-width:2px
    classDef aiLayer fill:#f3e5f5,stroke:#4a148c,stroke-width:2px
    classDef serverLayer fill:#e8f5e8,stroke:#1b5e20,stroke-width:2px
    classDef sharedLayer fill:#fff3e0,stroke:#e65100,stroke-width:2px
    classDef resultLayer fill:#fce4ec,stroke:#880e4f,stroke-width:2px
    
    class A,B userLayer
    class C,D,E,F aiLayer
    class I,L serverLayer
    class J,M,K sharedLayer
    class N,O,P,Q resultLayer
```

## Key Components

### User Interface Layer
- **User Input**: Natural language requests like "Read the hydra-README.md file"
- **Streamlit Frontend**: Web interface that handles user interaction

### AI Processing Layer
- **OpenAI GPT-4o-mini**: Analyzes user intent and decides on function calls
- **Function Selection**: Maps natural language to specific MCP tools
- **Tool Registry**: Maintains mapping between function names and MCP servers

### Server Layer
- **Files MCP Server** (Port 8002): Handles file operations (list, read, write)
- **API MCP Server** (Port 8001): Provides random facts

### Shared Components
- **FileOperations Class**: Core file handling logic
- **RandomFacts Class**: Fact management and selection
- **Shared Files Directory**: Common storage for both implementations

### Data Flow
1. User enters natural language request
2. Streamlit sends request to OpenAI with available tools
3. AI decides which function to call and with what parameters
4. Request routed to appropriate MCP server
5. Server uses shared components to perform operation
6. Result returned through HTTP to Streamlit
7. Result displayed to user

## Interactive Features (Future Enhancement)

This flowchart can be enhanced with:
- **Clickable boxes**: Each box could link to the corresponding code file
- **Animation**: Flow highlighting to show current execution path
- **Code popups**: Hover or click to show relevant code snippets
- **Live data**: Real-time status indicators for each component 