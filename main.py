from fastapi import FastAPI, Response, status
import sqlite3


from admin_db import construct_part, construct_part_list
app = FastAPI()

#LIST ALL PARTS
@app.get("/parts/list")
async def parts_list_all():
    from admin_db import parts_list_all
    return construct_part_list(parts_list_all())

#LIST PART BY ID
#TODO Error checking, if part is not found
@app.get("/parts/list/{part_id}")
async def parts_list_by_id(part_id: int):
    from admin_db import parts_list_by_id
    return  construct_part(parts_list_by_id(part_id))

#LIST MULTIPLE PARTS BY IDS
#TODO Error checking, if part is not found
@app.get("/parts/list/multiple/{part_ids}")
async def parts_list_by_ids(part_ids: str):
    from admin_db import parts_list_by_ids
    return construct_part_list(parts_list_by_ids(part_ids))

#SEARCH IN PARTS
#BY NAME
@app.get("/parts/search/{name}")
async def parts_search_by_name(name: str):
    from admin_db import parts_search_by_name
    return construct_part_list(parts_search_by_name(name))

#BY CATEGORY
@app.get("/parts/search/category/{category}")
async def parts_search_by_category(category: str):
    from admin_db import parts_search_by_category
    return construct_part_list(parts_search_by_category(category))

#BY SUBCATEGORY
@app.get("/parts/search/sub_category/{sub_category}")
async def parts_search_by_category(sub_category: str):
    from admin_db import parts_search_by_sub_category
    return construct_part_list(parts_search_by_sub_category(sub_category))

#CREATE PART
#TODO Create multiple parts, Error checking
@app.post("/parts/create")
async def parts_create(part: dict):
    from admin_db import parts_create
    return construct_part(parts_create(part))

#DELETE PARTS
#TODO make sure parts are deleted properly, Error checking
@app.delete("/parts/delete/{part_ids}")
async def parts_delete_by_ids(part_ids: str):
    from admin_db import parts_delete_by_ids
    rows = parts_delete_by_ids(part_ids)
    return rows

#UPDATE PART
#TODO Update multiple parts, Error checking
@app.put("/parts/update/{part_id}")
async def parts_update_by_id(part_id:int, parameters: dict):
    from admin_db import parts_update_by_id
    return construct_part(parts_update_by_id(part_id, parameters))

#LIST BORROWED PARTS
@app.get("/parts/borrowed/list")
async def parts_borrowed_list():
    from admin_db import parts_borrowed_list
    return construct_part_list(parts_borrowed_list())

#LIST BORROWED PARTS BY IDS
@app.get("/parts/borrowed/list/{part_ids}")
async def parts_borrowed_list_by_ids(part_ids: str):
    from admin_db import parts_borrowed_list_by_ids
    return construct_part_list(parts_borrowed_list_by_ids(part_ids))

#TODO make sure parts are deleted properly, Error checking
#DELETE BORROWED PARTS BY IDS
@app.delete("/parts/borrowed/delete/{part_ids}")
async def parts_borrowed_delete_by_ids(part_ids: str):
    from admin_db import parts_borrowed_delete_by_ids
    return parts_borrowed_delete_by_ids(part_ids)


#BORROW PARTS
#TODO in admin_db, works, but doesn't check min count
@app.post("/parts/borrow/{part_ids}/{counts}")
async def parts_update(part_ids: str, counts: str, response: Response):
    from admin_db import parts_borrow
    try:
        response.status_code = status.HTTP_200_OK
        return parts_borrow(part_ids, counts)
    except Exception as e:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"message": str(e)}

#TODO List and delete borrowed
#TODO History
#TODO Users
#TODO LIMITED COUNT/MIN COUNT