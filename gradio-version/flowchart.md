# Gradio Version - System Architecture Flow

## Interactive Flowchart

```mermaid
graph TD
    %% User Interface Layer
    A[User Input: Direct UI Actions] --> B[Gradio Frontend]
    
    %% Direct Function Calls
    B --> C{Action Type}
    
    %% File Operations Branch
    C -->|List Files| D[list_files Function]
    C -->|Read File| E[read_file Function]
    C -->|Write File| F[write_file Function]
    C -->|Random Fact| G[get_random_fact Function]
    
    %% Shared Components
    D --> H[FileOperations Class]
    E --> H
    F --> H
    G --> I[RandomFacts Class]
    
    %% Data Storage
    H --> J[Shared Files Directory]
    I --> K[Facts Collection]
    
    %% Results
    J --> L[File Results]
    K --> M[Random Fact]
    L --> N[Gradio Display]
    M --> N
    
    %% Styling
    classDef userLayer fill:#e1f5fe,stroke:#01579b,stroke-width:2px
    classDef functionLayer fill:#f3e5f5,stroke:#4a148c,stroke-width:2px
    classDef sharedLayer fill:#e8f5e8,stroke:#1b5e20,stroke-width:2px
    classDef dataLayer fill:#fff3e0,stroke:#e65100,stroke-width:2px
    classDef resultLayer fill:#fce4ec,stroke:#880e4f,stroke-width:2px
    
    class A,B userLayer
    class C,D,E,F,G functionLayer
    class H,I sharedLayer
    class J,K dataLayer
    class L,M,N resultLayer
```

## Key Components

### User Interface Layer
- **User Input**: Direct UI interactions (button clicks, text inputs)
- **Gradio Frontend**: Single-page web interface with tabs and forms

### Function Layer
- **list_files Function**: Lists all files in the shared directory
- **read_file Function**: Reads content of a specific file
- **write_file Function**: Creates or modifies files
- **get_random_fact Function**: Returns a random fact

### Shared Components
- **FileOperations Class**: Same core file handling logic as MCP version
- **RandomFacts Class**: Same fact management as MCP version

### Data Storage
- **Shared Files Directory**: Common storage (same as MCP version)
- **Facts Collection**: Built-in facts array

### Data Flow
1. User interacts directly with UI components
2. Gradio calls appropriate function based on user action
3. Function uses shared components to perform operation
4. Result returned directly to Gradio interface
5. Result displayed to user

## Comparison with MCP Version

### Simplicity
- **No AI processing**: Direct function calls instead of natural language interpretation
- **No servers**: Single process instead of distributed architecture
- **No HTTP**: Direct function calls instead of API requests

### Shared Benefits
- **Same business logic**: Uses identical shared components
- **Same data**: Operates on the same files and facts
- **Same functionality**: Provides identical features

## Interactive Features (Future Enhancement)

This flowchart can be enhanced with:
- **Clickable boxes**: Each box could link to the corresponding code file
- **Animation**: Flow highlighting to show current execution path
- **Code popups**: Hover or click to show relevant code snippets
- **Live data**: Real-time status indicators for each component 