"""

This file contains three functions that compute :math:`x[n+1]`, :math:`y[n+1]` 
and :math:`z[n+1]` based on known values of the system :math:`x[n]`, 
:math:`y[n]`and :math:`z[n]`

The last function implements these functions and gets called from a loop in 
the solver module.

"""


def forward_diff_x(sigma, x, y, dt):
    """

    Update equation for coordinate :math:`x`: 
        
        :math:`x[n+1] = \\sigma(y[n]-x[n])t_{\\delta} + x[n]`

    INPUT::
        
        sigma : float
            Prandtl number
        x : float
            Current value of coordinate x (x[n]).
        y : float
            Current value of coordinate y (y[n]).
        dt : float
            Time step (s).

    OUTPUT::
        
        float
            x at the next time step (x[n+1]).

    """

    return sigma * (y - x) * dt + x
    

def forward_diff_y(rho, x, y, z, dt):
    """

    Update equation for coordinate :math:`y`:
    
        :math:`y[n+1] = (x[n](\\rho - z[n]) - y[n])t_{\\delta} + y[n]`


    INPUT::
        
        rho : float
            Free parameter.
        x : float
            Current value of coordinate x (x[n]).
        y : float
            Current value of coordinate y (y[n]).
        z : float
            Current value of coordinate z (z[n]).
        dt : float
            Time step (s).

    OUTPUT::
        
        float
            y at the next time step (y[n+1]).

    """
    return (x * (rho - z) - y) * dt + y


def forward_diff_z(beta, x, y, z, dt):
    """

    Update equation for coordinate :math:`z`: 
        
        :math:`z[n+1] = (x[n]y[n] - \\beta z[n])t_{\\delta} + z[n]`

    INPUT::

        beta : float
            Free parameter.
        x : float
            Current value of coordinate x (x[n]).
        y : float
            Current value of coordinate y (y[n]).
        z : float
            Current value of coordinate z (z[n]).
        dt : float
            Time step (s).

    OUTPUT::
        
        float
            z at the next time step (z[n+1]).


    """

    return (x * y - beta * z) * dt + z



def update_system_state(x, y, z, sigma, beta, rho, dt):
    """

    Function to calculate the values of :math:`x`, :math:`y`, and :math:`z` 
    at the next time step (:math:`n+1`) using known values of
    these variables at the current time step (:math:`n`)


    INPUT::
        
        x : float
            Current value of coordinate x (x[n]).
        y : float
            Current value of coordinate y (y[n]).
        z : float
            Current value of coordinate z (z[n]).
        sigma : float
            Free parameter.
        beta : float
            Free parameter.
        rho : float
            Free parameter.
        dt : float
            Time step (s).


    OUTPUT::
        
        x_next : float
            Next value of coordinate x (x[n+1]).    
        y_next : float
            Next value of coordinate y (y[n+1]).
        z_next : float
            Next value of coordinate z (z[n+1]).

    """

    x_next = forward_diff_x(sigma, x, y, dt)
    y_next = forward_diff_y(rho, x, y, z, dt)
    z_next = forward_diff_z(beta, x, y, z, dt)

    return x_next, y_next, z_next