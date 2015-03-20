# Now you will write code for a function called 
# make_HTML_for_many_concepts. This function will take a list 
# of concepts (each of which is itself a list) and will return
# the appropriate string of HTML. 
#

def generate_concept_HTML(concept_title, concept_description):
    html_text_1 = '''
<div class="concept">
    <div class="concept-title">
        ''' + concept_title
    html_text_2 = '''
    </div>
    <div class="concept-description">
        ''' + concept_description
    html_text_3 = '''
    </div>
</div>'''
    
    full_html_text = html_text_1 + html_text_2 + html_text_3
    return full_html_text

def make_HTML(concept):
    concept_title = concept[0]
    concept_description = concept[1]
    return generate_concept_HTML(concept_title, concept_description)

# This is an example of what a list of concepts might look like.
EXAMPLE_LIST_OF_CONCEPTS = [ ['Python', 'Python is a Programming Language'],
                             ['For Loop', 'For Loops allow you to iterate over lists'],
                             ['Lists', 'Lists are sequences of data'] ]

# This is the function you will write.
def make_HTML_for_many_concepts(list_of_concepts):
    for e in list_of_concepts:
        print make_HTML(e)# write code here that generates the appropriate HTML
    # for a list of concepts.

print make_HTML_for_many_concepts(EXAMPLE_LIST_OF_CONCEPTS)
