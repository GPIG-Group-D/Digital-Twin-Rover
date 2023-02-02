from ursina.prefabs.first_person_controller import FirstPersonController


class Viewport(FirstPersonController):
    """
    Class to abstract the FirstPersonController Ursina class, this allows a floating camera
    """
    def input(self, key):
        """
        FirstPersonController input function override
        :param key:
        :return:
        """
        if key == 'space':
            self.position += (0, 0.03, 0)

        if key == 'shift':
            self.position -= (0, 0.03, 0)
