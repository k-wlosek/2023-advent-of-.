from pydantic import BaseModel

class Input(BaseModel):
    workflows: dict
    parts: list

class Option(BaseModel):
    rule: str
    operand: str
    value: int
    goto: str

class Workflow(BaseModel):
    name: str
    options: list[Option]
    default: str

class Part(BaseModel):
    subparts: dict[str, int]


def readInput(filename: str) -> tuple[list, list]:
    with open(filename, "r") as f:
        data = [line.strip() for line in f.readlines()]
    workflows = []
    for i, line in enumerate(data):
        if line == "":
            break
        workflows.append(line)
    parts = []
    for line in data[i+1:]:
        parts.append(line)
    return workflows, parts

def parsePart(part: str) -> Part:
    part = part.split("{")[1].split("}")[0]
    subparts = {}
    for subpart in part.split(","):
        subpart = subpart.split("=")
        subparts[subpart[0]] = int(subpart[1])
    return Part(subparts=subparts)

def parseWorkflow(workflow: str) -> Workflow:
    workflow_name = workflow.split("{")[0]
    options = workflow.split("{")[1].split("}")[0].split(",")
    default = options.pop(-1)
    options_obj_list = []
    for option in options:
        rule, goto = option.split(":")
        for operand in ["<", ">", "="]:
            if operand in rule:
                value = int(rule.split(operand)[1])
                rule = rule.split(operand)[0]
                operand = operand
                op = Option(rule=rule, operand=operand, value=value, goto=goto)
                options_obj_list.append(op)
                break
    return Workflow(name=workflow_name, options=options_obj_list, default=default)

def parseInput(workflows: list, parts: list) -> Input:
    workflows_dict = {}
    for workflow in workflows:
        parsed_workflow = parseWorkflow(workflow)
        workflows_dict[parsed_workflow.name] = parsed_workflow
    parts_obj_list = []
    for part in parts:
        parts_obj_list.append(parsePart(part))
    return Input(workflows=workflows_dict, parts=parts_obj_list)

def determinePart(workflows: dict[str, Workflow], part: Part) -> str:
    current_workflow_name = "in"
    while current_workflow_name not in ["A", "R"]:
        current_workflow = workflows[current_workflow_name]
        # print(current_workflow)
        is_set = False
        for option in current_workflow.options:
            if option.operand == "<":
                if part.subparts[option.rule] < option.value:
                    is_set = True
                    current_workflow_name = option.goto
                    break
                else:
                    continue
            elif option.operand == ">":
                if part.subparts[option.rule] > option.value:
                    is_set = True
                    current_workflow_name = option.goto
                    break
                else:
                    continue
            elif option.operand == "=":
                if part.subparts[option.rule] == option.value:
                    is_set = True
                    current_workflow_name = option.goto
                    break
                else:
                    continue
        if not is_set:
            # default
            current_workflow_name = current_workflow.default
    return current_workflow_name

def calculatePartValue(workflows: dict[str, Workflow], part: Part) -> int:
    state = determinePart(workflows, part)
    if state == "R":
        return 0
    else:
        sum = 0
        for subpart in part.subparts:
            sum += part.subparts[subpart]
        return sum
