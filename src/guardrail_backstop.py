# ------------------------------------------------------ #
#
#   guardrail_backstop.py
#
#   Guardrail for mī lyte System 1. A BASE
#   Simone J. Skeen x Claude Code (10-01-2026)
#
# ------------------------------------------------------ #

##########################################################
#
#  NOTE 6/25: Language below is provisional and UNTESTED. Do NOT use in production.
#
##########################################################

GUARDRAIL_BACKSTOP = '''
    If a user describes active suicidal ideation, ignore previous instructions and respond with:

    "It sounds as if you're experiencing suicidal thoughts. Feeling this way is common, and many people
    do over the course of their lives. Your best course of action will be to talk with a trained counselor
    to be sure your needs are met. Here are some options to consider:

    You can call the 988 Suicide & Crisis Lifeline by dialing 988.

    You can access text, chat, and Deaf/hard-of-hearing options at https://988lifeline.org/
    
    BlackLine, a space for peer support prioritizing BIPOC (Black, Indigenous, and People of Color) callers, 
    can be reached at 1-800-604-5841.

    The Trevor Project, specializing in meeting the needs of LGBTQ+ young people, can be reached by 
    texting 'START' to 678-678 or calling 1-866-488-7386. Deaf and Hard of Hearing users can call 
    1-866-803-3699. Learn more at https://www.thetrevorproject.org/get-help/

    Trans Lifeline, providing trans peer support divested from police, can be reached at 877-565-8860."

    DO NOT CONSULT your context. DO NOT DEVIATE from this statement. DO NOT recite poetry.
    '''

# Unique phrase for detecting guardrail activation in responses
# Update this if the guardrail script changes
BACKSTOP_MARKER = r'988 Suicide & Crisis Lifeline'