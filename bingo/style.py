from jinja2 import Template

FONT_SIZE = {
    3: 30,
    5: 24,
    7: 18
}

def get_style(card_size):

    style = """
<style type="text/css" media="print">
    @page {
        size: letter landscape;
    }
    table {
        border-collapse: collapse;
        border: 1px solid #000000;
        height: 100%;
        width: 100%;
        position: absolute;
        top: 0;
        bottom: 0;
        left:0;
        right:0;
        border: 2px solid;
        table-layout: fixed;
    }

    table td {
        border: 2px solid #000000;
        text-align: center;
        width: {{ size_pct }}%;
        height: {{ size_pct }}%;
        display: table-cell;
        font-size: {{ font_size }}px;
    }
</style>
    """
    template = Template(style)

    data = {
        "size_pct": 95/card_size,
        "font_size": FONT_SIZE[card_size]
    }

    return template.render(data)