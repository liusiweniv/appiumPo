import  yaml
def test_yaml():
    with open("../page/main.yml", encoding='utf-8') as f:
        steps = yaml.safe_load(f)
    for step in  steps:
        if 'by' in step.keys():
            print('查找元素')
        if 'action' in step.keys():
            print("动作解析")
            action = step['action']
            if action == 'click':
                print("click操作")

            if action == 'send':
                value = step['value']
                print(f'send{value}')

    print(step)