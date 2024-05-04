from PySide6.QtCore import QObject, Signal


class MujocoViewerSignaler(QObject):
    """
    A class for emitting signals related to MujocoViewer actions.

    Attributes:
        signaler (Signal): A general signal used to emit data related to a MujocoViewer action.
        revolve_signal (Signal): A signal emitted when a revolve action is performed in MujocoViewer.
        step_finished_signal (Signal): A signal emitted when a step is finished in MujocoViewer.

    """
    signaler = Signal(object, object)
    revolve_signal = Signal(object, object)
    step_finished_signal = Signal(object, object)

    def __init__(self):
        """
            Initialize the MujocoViewerSignaler.
        """
        super(MujocoViewerSignaler, self).__init__()

    def throw_signal(self, model: object, data: object):
        """
        Emit a general signal with the provided model and data.

        Args:
            model (object): The model related to the signal.
            data (object): The data associated with the signal.
        """
        self.signaler.emit(model, data)


mujoco_signal = MujocoViewerSignaler()
