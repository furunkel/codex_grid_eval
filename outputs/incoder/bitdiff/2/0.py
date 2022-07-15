
def bit_diff(a, b):
    """
    Returns whether the two numbers differ at exactly one bit position.
    """
    return a ^ b

# ______________________________________________________________________________
# Misc functions

class injection:
    """
    A decorator used to inject a given object into a class hierarchy.
    Useful for simulating dependencies between components.
    Any component that gets injected into another component is
    dependent on the dependency to also be injected into
    the first component. This dependency can even be mutually
    dependent.

    When injecting a component into another component, the two
    components are usually combined as one component and then
    placed into the same top-level container. The top-level container
    usually corresponds to a physical piece of hardware. Components
    are often grouped in libraries, which are independent design
    elements. A library can contain any number of components and
    these components can be used independently or in combination
    with each other. Components can also be designated as injection
    targets, which allows them to be swapped in or out of existence
    anywhere in the hierarchy.

    For example, a robot might have an injection target that represents
    a power supply and various components that control its operation.
    Depending on what kind of power supply is connected to the robot,
    different components can be used or combined to perform different
    operations. Power supplies are injected into the robot component
    so that it can control its operation. Different power supplies
    might be used to control different motors, or to control various
    aspects of the robot's operation (e.g. turn speed, steering angle).
    These power supplies might have different capabilities (physical
    capabilities) and/or different operating characteristics (operation
    characteristics).

    Power supplies are often grouped into libraries, which are independent
    design elements. A library can contain any number of power supplies
    and these power supplies can be independently used or in combination
    with each other. Power supplies can also be designated as injection
    targets, which allows them to be swapped in or out of existence
    anywhere in the hierarchy.

    For example, a robot might have an injection target that represents
    a power supply and various components that control its operation.
    Depending on what kind of power supply is connected to the robot,
    different components can be used or combined to perform different
    operations. Power supplies are injected into the robot component
    so that it can control its operation. Different power supplies
    might be used to control different motors, or to control various
    aspects of the robot's operation (e.g. turn speed, 