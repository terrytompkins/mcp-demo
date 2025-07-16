I need to create presentation-ready interactive flowcharts for this project. Please analyze the codebase and create the following artifacts:

### **Requirements:**
1. **Create a Mermaid.js flowchart** that shows the system architecture and data flow
2. **Create an interactive HTML viewer** with clickable components and code popups
3. **Use consistent styling** and structure across all diagrams
4. **Focus on key components** and their relationships, not every detail

### **Deliverables:**

#### **1. Flowchart Markdown File** (`flowchart.md`)
- Use Mermaid.js syntax with `graph TD` (top-down direction)
- Include color-coded sections using `classDef` and `class` statements
- Show data flow with arrows and decision points
- Add detailed comments explaining each section
- Include a "Key Components" section explaining the architecture

#### **2. Interactive HTML File** (`interactive-flowchart.html`)
- Self-contained HTML file with embedded Mermaid.js
- Professional styling with modern CSS
- Clickable component cards below the flowchart
- Code popup functionality for each component
- Responsive design that works on different screen sizes

### **HTML Structure Requirements:**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>[Project Name] - Interactive Flowchart</title>
    <script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
    <style>
        /* Professional styling with:
           - Clean, modern design
           - Color-coded sections
           - Responsive grid layouts
           - Hover effects
           - Modal popups for code
        */
    </style>
</head>
<body>
    <div class="overlay" id="overlay"></div>
    
    <div class="container">
        <h1>[Project Name] - Interactive System Architecture</h1>
        
        <div class="flowchart-container">
            <div class="mermaid" id="flowchart">
                <!-- Mermaid.js flowchart here -->
            </div>
        </div>

        <div class="component-info">
            <h2>Component Details</h2>
            <div class="component-grid">
                <!-- Component cards with:
                     - Component name and description
                     - Key functionality
                     - Links to relevant code files
                     - onclick="showCode('filename')" for popups
                -->
            </div>
        </div>
    </div>

    <div class="code-popup" id="codePopup">
        <button class="close-btn" onclick="closePopup()">×</button>
        <h3 id="popupTitle">Code View</h3>
        <pre id="popupContent"></pre>
    </div>

    <script>
        mermaid.initialize({ 
            startOnLoad: true,
            theme: 'default',
            flowchart: {
                useMaxWidth: true,
                htmlLabels: true
            }
        });

        function showCode(filename) {
            // Popup logic with code samples
        }

        function closePopup() {
            // Close popup logic
        }
    </script>
</body>
</html>
```

### **Flowchart Design Guidelines:**
- **Use meaningful node names** that correspond to actual code components
- **Color-code by layer/function**: UI, business logic, data, external services
- **Show data flow** with clear arrows and labels
- **Include decision points** for conditional logic
- **Group related components** visually
- **Keep it readable** - don't overcrowd with too many nodes

### **Component Card Guidelines:**
- **Group by architectural layer** (UI, Services, Data, etc.)
- **Include key functionality** description
- **Link to actual source files** when possible
- **Provide code samples** for important functions
- **Use consistent terminology** with the codebase

### **Code Popup Guidelines:**
- **Include relevant code snippets** for each component
- **Show key functions/methods** that demonstrate the component's purpose
- **Keep snippets focused** - don't show entire files
- **Use syntax highlighting** if possible
- **Include file paths** for reference

### **Analysis Instructions:**
1. **Scan the codebase** to identify main components and their relationships
2. **Identify the entry points** (main functions, API endpoints, UI components)
3. **Map data flow** between components
4. **Identify key decision points** and conditional logic
5. **Group components** by architectural responsibility
6. **Select representative code samples** for each component

### **Output Location:**
- Place both files in the project root directory
- Use descriptive filenames: `flowchart.md` and `interactive-flowchart.html`

Please analyze this project and create these interactive flowcharts following the pattern above. Focus on making them presentation-ready and visually engaging while accurately representing the system architecture.