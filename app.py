import gradio as gr  # load gradio
import random  # used for generating random numbers

def bubble_sort_steps(nums_string):  # bubble sort function
    try:
        arr = [int(x.strip()) for x in nums_string.split(",")]  # turn string into list of integers
    except:
        return "Error: enter numbers separated by commas."  # show if input is invalid

    steps = []  # list of lines to display
    a = arr.copy()  # [AI] work on a copy of the list
    n = len(a)  # get the size of the list

    steps.append(f"STARTING LIST: {a}<br><br>")  # show original list

    for i in range(n):  # each pass through the list
        steps.append("------------------------------<br>")  # separator
        steps.append(f"Pass {i+1}<br>")  # show which pass we are on

        for j in range(0, n - i - 1):  # compare pairs
            steps.append(f"Comparing {a[j]} and {a[j+1]}<br>")  # show comparison

            if a[j] > a[j+1]:  # if out of order
                steps.append(f"Swap: {a[j]} with {a[j+1]}<br>")  # show swap
                a[j], a[j+1] = a[j+1], a[j]  # do the swap
                steps.append(f"Result: {a}<br><br>")  # show updated list
            else:
                steps.append("No swap<br>")  # no change
                steps.append(f"Result: {a}<br><br>")  # show list unchanged

    steps.append("------------------------------<br>")  # final separator
    steps.append("FINISHED<br>")  # final label
    steps.append(f"FINAL LIST: {a}")  # final sorted result

    return "".join(steps)  # [AI] return all lines joined as HTML

def generate_random_list(length, max_value):  # function to create random list
    lst = [random.randint(0, max_value) for _ in range(length)]  # [AI] build list of random numbers
    return ", ".join(str(x) for x in lst)  # [AI] return as comma-separated string



input_numbers = gr.Textbox(  # type input for bubble sort
    label="Enter numbers separated by commas",
    placeholder="Example: 5, 2, 7, 3"
)

output_text = gr.Markdown()  # [AI] markdown output

length_slider = gr.Slider(  # choose length of random list
    minimum=1,
    maximum=20,
    step=1,
    value=5,
    label="List Length (max 20)"
)

range_slider = gr.Slider(  # choose max value for random numbers
    minimum=1,
    maximum=1000,
    step=1,
    value=100,
    label="Max Number Value (0 to 1000)"
)

generate_button = gr.Button("Generate Random List")  # button that creates list




app = gr.Blocks()  # using Blocks so we can layout components

with app:
    gr.Markdown("## Bubble Sort Visualizer")  #title
    gr.Markdown("Shows bubble sort step-by-step in a clear format.")  # description

    with gr.Row():  # row for the random list controls
        length_slider.render()
        range_slider.render()
        generate_button.render()

    generate_button.click(  # when button is pressed
        fn=generate_random_list,  # call random list generator
        inputs=[length_slider, range_slider],  # takes slider values
        outputs=input_numbers  # fills the textbox automatically
    )

    input_numbers.render()  # show the input box

    sort_button = gr.Button("Run Bubble Sort")  # button to run the sort

    sort_button.click(  # when sort button is pressed
        fn=bubble_sort_steps,  # run bubble sort
        inputs=input_numbers,  # take whatever is in the textbox
        outputs=output_text  # show steps
    )

    output_text.render()  #output


app.launch(inbrowser=True)  # open in browser automatically
