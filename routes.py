import aiofiles.os
from aiohttp import web

import const
from utils import get_files
from utils import delete_file
from utils import get_file_path
from utils import get_hash
from utils import save_file
from utils import is_exist

routes = web.RouteTableDef()


@routes.view("/files")
class ListFileView(web.View):

    async def get(self):
        files = get_files(const.STORAGE_FOLDER)
        data = [{'filename': file} for file in files]
        return web.json_response(data=data)


@routes.view("/file/{hash_file}")
class OperationsFileView(web.View):

    async def get(self):
        filename = self.request.match_info['hash_file']
        if len(filename) != 32:
            return web.HTTPBadRequest()
        path = await get_file_path(filename)
        if not is_exist(path):
            return web.HTTPNotFound()
        return web.FileResponse(path)

    async def delete(self):
        filename = self.request.match_info['hash_file']
        if len(filename) != 32:
            return web.HTTPBadRequest()
        result = await delete_file(filename)
        if result:
            return web.HTTPOk()
        return web.HTTPNotFound()


@routes.view("/file/")
class UploadFileView(web.View):

    async def post(self):
        data = await self.request.post()
        if 'file' not in data:
            return web.HTTPBadRequest()
        file = data['file'].file
        filename = get_hash(file)
        result = await save_file(filename, file)
        return web.json_response(data={'filename': result})
