from langchain import OpenAI, PromptTemplate

prompt_placeholder = '[$$$]'

data_format = {'name': '', 'title': '',
               'contactInfo': {'linkedin': '', 'github': '', 'email': '', 'address': '', 'phone': ''}, 'summary': '',
               'workExperience': [{'title': '', 'company': '', 'dates': '', 'description': ''},
                                  {'title': '', 'company': '', 'dates': '', 'description': ''}, ],
               'education': [{'degree': '', 'school': '', 'dates': '', 'description': ''}, ], 'skills': ['', '', '']}

recruiter_prompt = 'You are a recruiter and a professional resume builder.'
command_prompt = 'Re-write the input as professionally as possible, adding vital and valuable information.'
user_request_prompt = f'{prompt_placeholder}'

output_commands_prompts = dict()
output_commands_prompts['all'] = f'Return the output as dictionary in the next format {str(data_format)}.'
output_commands_prompts['section'] = f'Return the output as string.'

input_prompt = f'Input: {prompt_placeholder}'


def get_prompt(input_data, user_request='', output_type='all'):
    input_data = str(input_data)
    valid_output_types = list(output_commands_prompts)
    assert str(output_type) in valid_output_types, f"Not valid output type, try {valid_output_types}"

    if user_request:
        user_request += '\n'

    template = '\n'.join(
        [recruiter_prompt, command_prompt, user_request_prompt.replace(prompt_placeholder, user_request),
         input_prompt.replace(prompt_placeholder, input_data), output_commands_prompts[output_type]])
    return template

