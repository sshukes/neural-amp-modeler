Training locally with the GUI
=============================

After installing NAM locally, you can launch the GUI trainer from a terminal 
with:

.. code-block:: console

    $ nam

Windows quick start
-------------------

#. Install dependencies and create/activate a virtual environment.
#. Install NAM and launch the GUI with ``nam``.
#. Export your reamp as a 48 kHz / 24-bit WAV file.
#. Train and save your model to a folder you control.

You'll see a GUI like this:

.. image:: media/gui/gui.png
    :scale: 30 %

Start by pressing the "Download input file" button to be taken to download the 
audio you'll reamp through your gear to make your model,
`input.wav <https://drive.google.com/file/d/1KbaS4oXXNEuh2aCPLwKrPdf5KFOjda8G/view?usp=sharing>`_.
Reamp this through the gear that you want to model and render the output as a
WAVE file. Be sure to match the sample rate (48k) and bit depth (24-bit) of the 
input file. Also, be sure that your render matches the length of the input file.
An example can be found here:
`output.wav <https://drive.google.com/file/d/1NrpQLBbCDHyu0RPsne4YcjIpi5-rEP6w/view?usp=sharing>`_.

Return to the trainer and pick the input and output files as well as where you
want your model to be saved.

.. note:: To train a batch of models, pick all of their reamp (output) files.

Once you've selected these, then the "Train" button should become available:

.. image:: media/gui/ready-to-train.png
    :scale: 30 %

Click "Train", and the program will check your files for any problems, then
start training.

Some recording setups will have round-trip latency that should be accounted for.
Some DAWs might attempt to compensate for this but can overcompensate. 
The trainer will automatically attempt to line up the input and output audio. To 
help with this, the input file has two impulses near its beginning that are used
to help with alignment. The trainer will attempt to identify the response to
these in the output. You'll see a plot showing where it thinks that the output
first reacted to the input (black dashed line) as well as the two responses
overlaid with each other. You should see that they overlap and that the black
line is just before the start of the response, like this:

.. image:: media/gui/impulse-responses.png
    :scale: 50 %

Close this figure, and then you will see training proceed. At the end, you'll
see a plot that compares the model's prediction against your recording:

.. image:: media/gui/result.png
    :scale: 30 %

Close that plot, and your model will be saved. To use it, point 
`the plugin <https://github.com/sdatkinson/NeuralAmpModelerPlugin>`_ at the file
and you're good to go!

Windows setup and tips
----------------------

Installing dependencies and activating the environment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Install Python 3.10+ (from python.org) and Git. Then, from PowerShell in the
repository root:

.. code-block:: console

    PS> py -3 -m venv .venv
    PS> .\.venv\Scripts\Activate.ps1
    PS> python -m pip install --upgrade pip
    PS> pip install -e .

If you are using Command Prompt instead of PowerShell, activate with:

.. code-block:: console

    C:\> .\.venv\Scripts\activate.bat

Launching the GUI
^^^^^^^^^^^^^^^^^

With the environment activated, run:

.. code-block:: console

    PS> nam

If the ``nam`` entry point is not on your PATH, you can use:

.. code-block:: console

    PS> python -m nam.train.gui

Windows file locations
^^^^^^^^^^^^^^^^^^^^^^

* GUI parameter history is stored in
  ``%USERPROFILE%\.nam\train_gui\parameters.json``.
* The GUI also saves its last-used paths in the installed package directory
  (``...\\site-packages\\nam\\train\\gui\\_resources\\settings.json``). This
  location depends on where Python is installed.
* Trained models are saved wherever you choose in the GUI, so pick a folder
  you own (for example, ``%USERPROFILE%\\Documents\\NAM Models``).

Windows audio export settings and troubleshooting
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Export or render as PCM WAV at 48 kHz / 24-bit (mono if possible).
* Disable any automatic sample-rate conversion, normalization, or
  loudness/podcast processing in your DAW or audio editor.
* If the trainer warns about sample rate or bit depth, re-export using the
  exact 48 kHz / 24-bit settings and verify the file length matches the input.
