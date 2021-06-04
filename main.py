from aiohttp import web
from data_analysis import extract_columns
app = web.Application()
routes = web.RouteTableDef()

@routes.get('/analyze_data')
async def upload(request):
    extract_columns(request.input_file, request.file_to_read, request.output_file)

if __name__ == "__main__":
    web.run_app(app, host='0.0.0.0', port=80)