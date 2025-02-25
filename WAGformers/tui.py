import pytermgui as ptg
import wag_tranform as wt

CONFIG = """
config:
    InputField:
        styles:
            prompt: dim italic
            cursor: '@72'
    Label:
        styles:
            value: dim bold

    Window:
        styles:
            border: '60'
            corner: '60'

    Container:
        styles:
            border: '96'
            corner: '96'
"""

def _use_gpt2(manager: ptg.WindowManager, amount: int, format: str) -> None:
    wt.useGPT2Transformer(amount, format) 

    modal = ptg.Window(
        "Run has finished",
        ptg.Container(
            ptg.Splitter(
                ptg.Button("Quit", lambda *_: manager.stop()),
                ptg.Button("New Run!!", lambda *_: modal.close()),
            ),
        ),
    ).center()

    modal.select(1)
    manager.add(modal)

def _use_bert(manager: ptg.WindowManager, amount: int, format: str) -> None:
    wt.useBERTTransformer(amount, format) 

    modal = ptg.Window(
        "Run has finished",
        ptg.Container(
            ptg.Splitter(
                ptg.Button("Quit", lambda *_: manager.stop()),
                ptg.Button("Go Back", lambda *_: modal.close()),
            ),
        ),
    ).center()

    modal.select(1)
    manager.add(modal)    

def _confirm_quit(manager: ptg.WindowManager) -> None:
    """Creates an "Are you sure you want to quit" modal window"""

    modal = ptg.Window(
        "Are you sure you want to quit?",
        "",
        ptg.Container(
            ptg.Splitter(
                ptg.Button("Yes", lambda *_: manager.stop()),
                ptg.Button("No", lambda *_: modal.close()),
            ),
        ),
    ).center()

    modal.select(1)
    manager.add(modal)

with ptg.YamlLoader() as loader:
    loader.load(CONFIG)

with ptg.WindowManager() as manager:
    amount = 50;

    file_format_input = ptg.InputField("", prompt="File Format: ")
    gen_amount_input =  ptg.InputField("", prompt="Sample amount: ")

    window = (
        ptg.Window(
            ptg.Container(
                "Notes:",
                ptg.Container(
                    "Welcome to the experimental version of the transformer generator, \nspecifically create to generate samples for WAG.", multiline=True
                ),
                box="EMPTY_VERTICAL",
            ),
            "",
            file_format_input,
            gen_amount_input,
            "",
            ptg.Container(
                ptg.Splitter(
                    ptg.Button("Bert", lambda *_: _use_bert(manager, int(gen_amount_input.value), file_format_input.value)),
                    ptg.Button("GPT2", lambda *_: _use_gpt2(manager, int(gen_amount_input.value), file_format_input.value)),
                ),
                static_width=60,
            ),
            "",
            "",
            ptg.Window(
                ptg.Button("Quit", lambda *_: _confirm_quit(manager)),
                box="EMPTY",
            ),
            width=60,
            box="DOUBLE",
        )
        .set_title("[210 bold]Wag Transformer Generator.")
        .center()
    )

    manager.add(window)