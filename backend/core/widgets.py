from django import forms
from django.utils.safestring import mark_safe
import json


class ContentBlocksWidget(forms.Widget):
    """Custom widget for managing content blocks with a user-friendly interface"""
    
    template_name = 'admin/content_blocks_widget.html'
    
    class Media:
        css = {
            'all': ('admin/css/content_blocks.css',)
        }
        js = ('admin/js/content_blocks.js',)
    
    def format_value(self, value):
        """Convert the value to the format expected by the widget"""
        if value is None:
            return []
        elif isinstance(value, str):
            try:
                return json.loads(value)
            except:
                return []
        elif isinstance(value, list):
            return value
        return []
    
    def render(self, name, value, attrs=None, renderer=None):
        # Use format_value to normalize the value
        value = self.format_value(value)
        
        # Generate HTML for the widget
        html = f'''
        <div class="content-blocks-widget" id="content-blocks-container">
            <div class="blocks-list" id="blocks-list">
        '''
        
        # Render existing blocks
        for index, block in enumerate(value):
            block_type = block.get('type', 'paragraph')
            content = block.get('content', '')
            
            if block_type == 'list' and isinstance(content, list):
                content = '\n'.join(content)
            
            html += self._render_block(index, block_type, content)
        
        html += '''
            </div>
            <div class="button-group">
                <button type="button" class="add-block-btn" onclick="addContentBlock()">
                    <span>+</span> Add Content Block
                </button>
                <button type="button" class="delete-all-btn" onclick="deleteAllBlocks()">
                    <span>×</span> Delete All Content
                </button>
            </div>
            <input type="hidden" name="{name}" id="content-blocks-data" value="">
        </div>
        
        <script>
        let blockCounter = {count};
        
        function addContentBlock() {{
            const blocksList = document.getElementById('blocks-list');
            const newBlock = createBlockElement(blockCounter, 'paragraph', '');
            blocksList.appendChild(newBlock);
            blockCounter++;
            updateHiddenField();
        }}
        
        function deleteAllBlocks() {{
            if (confirm('Are you sure you want to delete ALL content blocks? This cannot be undone.')) {{
                const blocksList = document.getElementById('blocks-list');
                blocksList.innerHTML = '';
                updateHiddenField();
            }}
        }}
        
        function createBlockElement(index, type, content) {{
            const div = document.createElement('div');
            div.className = 'content-block';
            div.dataset.index = index;
            div.innerHTML = `
                <div class="block-header">
                    <select class="block-type-select" onchange="handleTypeChange(this, ${{index}})">
                        <option value="paragraph" ${{type === 'paragraph' ? 'selected' : ''}}>Paragraph</option>
                        <option value="heading" ${{type === 'heading' ? 'selected' : ''}}>Heading</option>
                        <option value="list" ${{type === 'list' ? 'selected' : ''}}>List</option>
                    </select>
                    <button type="button" class="move-up-btn" onclick="moveBlockUp(${{index}})" title="Move Up">↑</button>
                    <button type="button" class="move-down-btn" onclick="moveBlockDown(${{index}})" title="Move Down">↓</button>
                    <button type="button" class="delete-block-btn" onclick="deleteBlock(${{index}})" title="Delete">×</button>
                </div>
                <div class="block-content">
                    ${{type === 'list' ? 
                        `<textarea class="block-textarea" placeholder="Enter list items (one per line)" oninput="updateHiddenField()">${{content}}</textarea>
                         <small class="help-text">Enter one item per line</small>` :
                        `<textarea class="block-textarea" placeholder="Enter content..." oninput="updateHiddenField()">${{content}}</textarea>`
                    }}
                </div>
            `;
            return div;
        }}
        
        function handleTypeChange(select, index) {{
            const block = select.closest('.content-block');
            const contentDiv = block.querySelector('.block-content');
            const textarea = contentDiv.querySelector('textarea');
            const currentContent = textarea.value;
            const newType = select.value;
            
            if (newType === 'list') {{
                contentDiv.innerHTML = `
                    <textarea class="block-textarea" placeholder="Enter list items (one per line)" oninput="updateHiddenField()">${{currentContent}}</textarea>
                    <small class="help-text">Enter one item per line</small>
                `;
            }} else {{
                contentDiv.innerHTML = `
                    <textarea class="block-textarea" placeholder="Enter content..." oninput="updateHiddenField()">${{currentContent}}</textarea>
                `;
            }}
            updateHiddenField();
        }}
        
        function deleteBlock(index) {{
            const block = document.querySelector(`[data-index="${{index}}"]`);
            if (block && confirm('Delete this content block?')) {{
                block.remove();
                updateHiddenField();
            }}
        }}
        
        function moveBlockUp(index) {{
            const block = document.querySelector(`[data-index="${{index}}"]`);
            const prev = block.previousElementSibling;
            if (prev) {{
                block.parentNode.insertBefore(block, prev);
                updateHiddenField();
            }}
        }}
        
        function moveBlockDown(index) {{
            const block = document.querySelector(`[data-index="${{index}}"]`);
            const next = block.nextElementSibling;
            if (next) {{
                block.parentNode.insertBefore(next, block);
                updateHiddenField();
            }}
        }}
        
        function updateHiddenField() {{
            const blocks = document.querySelectorAll('.content-block');
            const data = [];
            
            blocks.forEach(block => {{
                const type = block.querySelector('.block-type-select').value;
                const textarea = block.querySelector('.block-textarea');
                let content = textarea.value;
                
                if (type === 'list') {{
                    content = content.split('\\n').filter(line => line.trim() !== '');
                }}
                
                if (content && (typeof content === 'string' ? content.trim() : content.length > 0)) {{
                    data.push({{ type, content }});
                }}
            }});
            
            document.getElementById('content-blocks-data').value = JSON.stringify(data);
        }}
        
        // Initialize on page load
        document.addEventListener('DOMContentLoaded', function() {{
            updateHiddenField();
        }});
        </script>
        
        <style>
        .content-blocks-widget {{
            background: #f8f9fa;
            padding: 20px;
            border-radius: 8px;
            border: 1px solid #ddd;
        }}
        
        .blocks-list {{
            margin-bottom: 15px;
        }}
        
        .content-block {{
            background: white;
            border: 2px solid #e0e0e0;
            border-radius: 8px;
            padding: 15px;
            margin-bottom: 15px;
            transition: all 0.3s;
        }}
        
        .content-block:hover {{
            border-color: #417690;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }}
        
        .block-header {{
            display: flex;
            gap: 10px;
            margin-bottom: 10px;
            align-items: center;
        }}
        
        .block-type-select {{
            flex: 1;
            padding: 8px 12px;
            border: 1px solid #ccc;
            border-radius: 4px;
            font-size: 14px;
            background: white;
        }}
        
        .move-up-btn, .move-down-btn, .delete-block-btn {{
            padding: 6px 12px;
            border: 1px solid #ccc;
            border-radius: 4px;
            background: white;
            cursor: pointer;
            font-size: 16px;
            transition: all 0.2s;
        }}
        
        .move-up-btn:hover, .move-down-btn:hover {{
            background: #417690;
            color: white;
            border-color: #417690;
        }}
        
        .delete-block-btn {{
            color: #dc3545;
            font-size: 20px;
            font-weight: bold;
        }}
        
        .delete-block-btn:hover {{
            background: #dc3545;
            color: white;
            border-color: #dc3545;
        }}
        
        .block-content {{
            margin-top: 10px;
        }}
        
        .block-textarea {{
            width: 100%;
            min-height: 100px;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 4px;
            font-family: inherit;
            font-size: 14px;
            resize: vertical;
        }}
        
        .block-textarea:focus {{
            outline: none;
            border-color: #417690;
            box-shadow: 0 0 0 3px rgba(65, 118, 144, 0.1);
        }}
        
        .help-text {{
            display: block;
            margin-top: 5px;
            color: #666;
            font-size: 12px;
        }}
        
        .add-block-btn {{
            width: 100%;
            padding: 12px;
            background: #417690;
            color: white;
            border: none;
            border-radius: 6px;
            font-size: 15px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s;
        }}
        
        .add-block-btn:hover {{
            background: #2e5a6f;
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(65, 118, 144, 0.3);
        }}
        
        .add-block-btn span {{
            font-size: 20px;
            margin-right: 5px;
        }}
        
        .button-group {{
            display: flex;
            gap: 10px;
        }}
        
        .delete-all-btn {{
            flex: 1;
            padding: 12px;
            background: #dc3545;
            color: white;
            border: none;
            border-radius: 6px;
            font-size: 15px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s;

        </style>
        '''.format(name=name, count=len(value))
        
        return mark_safe(html)
    
    def _render_block(self, index, block_type, content):
        if isinstance(content, list):
            content = '\n'.join(content)
        
        content = str(content).replace('"', '&quot;').replace("'", '&#39;')
        
        help_text = '<small class="help-text">Enter one item per line</small>' if block_type == 'list' else ''
        
        return f'''
        <div class="content-block" data-index="{index}">
            <div class="block-header">
                <select class="block-type-select" onchange="handleTypeChange(this, {index})">
                    <option value="paragraph" {'selected' if block_type == 'paragraph' else ''}>Paragraph</option>
                    <option value="heading" {'selected' if block_type == 'heading' else ''}>Heading</option>
                    <option value="list" {'selected' if block_type == 'list' else ''}>List</option>
                </select>
                <button type="button" class="move-up-btn" onclick="moveBlockUp({index})" title="Move Up">↑</button>
                <button type="button" class="move-down-btn" onclick="moveBlockDown({index})" title="Move Down">↓</button>
                <button type="button" class="delete-block-btn" onclick="deleteBlock({index})" title="Delete">×</button>
            </div>
            <div class="block-content">
                <textarea class="block-textarea" placeholder="{'Enter list items (one per line)' if block_type == 'list' else 'Enter content...'}" oninput="updateHiddenField()">{content}</textarea>
                {help_text}
            </div>
        </div>
        '''
    
    def value_from_datadict(self, data, files, name):
        """Extract value from form data"""
        value = data.get(name, '[]')
        
        # If it's already a list, convert to JSON string for storage
        if isinstance(value, list):
            return value
        
        # If it's a string, parse it and return as list
        if isinstance(value, str):
            try:
                parsed = json.loads(value) if value else []
                return parsed
            except:
                return []
        
        return []
