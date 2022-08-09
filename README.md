# TaskScript
 You can manage the tasks with the script 

## feature

TaskScript.py --init <br />
TaskScript.py --add "category" "description" "status" <br />
TaskScript.py --show "category" <br />
TaskScript.py --delete "category"  <br />

Functions : 
| name | Application | argumnets | 
| ---- | ----------- | --------- |
| init | create table in data base | None | 
| display | show tasks | task_category  = None | 
| insert | add task into database| task_category , task_msg  , task_status | 
| delete | delete task(s) | category (optional) | 

## Usage Modules  : 
docopt 
tabulate 

