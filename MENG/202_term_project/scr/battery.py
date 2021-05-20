"""
battery.py includes the definition of a battery class 

"""



# Default storage capacity of Battery
_DEFAULT_STORAGE = 100.0
# Default input rate
_DEFAULT_IN_RATE = 20.0
# Default output rate
_DEFAULT_OUT_RATE = 10.0
# Default total effeciency
_DEFAULT_EFFICIENCY = 0.9


class Battery:
    """
    Battery unit properties and methods

    :attr max_capcity: The maximum amount of "stuff" that can be stored (float: arbitrary units of stuff = n)
    :attr capacity: Units stored in battery currenly (float: stuff-n)
    :attr flow_out: How many units of stuff per unit time can leave the battery (float: - dn/dt)
    :attr flow_in:  How many units of stuff per unit time can enter the battery (float: + dn/dt)
    :attr input_time: How much time the last uptake/charge cycle took (float: time-t)
    :attr output_time: How much time the last output cycle took (float: time-t)
    :attr round_trip_eff: Portion of stuff put into the Battery can be retrieved (float: [0.0,1.0])
    """

    def __init__(
        self,
        storage_potential=_DEFAULT_STORAGE,
        f_in=_DEFAULT_IN_RATE,
        f_out=_DEFAULT_OUT_RATE,
        effc=_DEFAULT_EFFICIENCY,
    ):
        """
        :param storage_potential: Total storage potential of cell (float: n)
        :param f_in: Maximum uptake/charge rate of stuff into cell - (Non-negative float)
        :param f_out: Maximum output rate of stuff out of cell (Non-negative float)
        :param effc: Storage efficiency of cell - See attr round_trip_eff (float: [0.0, 1.0])
        """
        assert all(
            [
                isinstance(storage_potential, float)
                or isinstance(storage_potential, int),
                (isinstance(f_in, float) or isinstance(f_in, int)) and not f_in < 0,
                (isinstance(f_out, float) or isinstance(
                    f_out, int)) and not f_out < 0,
                isinstance(effc, float) or isinstance(effc, int),
            ]
        )

        self.max_capacity = self.capacity = storage_potential
        self.flow_out, self.flow_in = f_out, f_in
        self.input_time = self.output_time = 0
        self.round_trip_eff = effc

    def get_charge_pct(self):
        """
        Percent of max_capacity currently occupied
        """
        return self.capacity / self.max_capacity

    def store(self, q):
        """
        Take in q amount of stuff into storage

        :param q: amount of stuff (float)
        """
        self.input_time = 0
        storage_pot = self.max_capacity - self.capacity
        if q < storage_pot:
            self.capacity += q
            self.input_time += q / self.flow_in
        else:
            self.capacity = self.max_capacity
            self.input_time += storage_pot / self.flow_in

    def output(self, q):
        """
        Take `q` amount of stuff out of storage accounting for 
        the turnarround in-efficiency
        will print a warning if it can't meet the demand `q`

        :param q: amount of stuff
        """
        assert isinstance(q, float) or isinstance(q, int)

        self.output_time = 0
        if q > self.capacity:
            qp = self.capacity
        else:
            qp = q

        q_req = qp / self.round_trip_eff
        if q_req > self.capacity:
            self.capacity -= qp
            q_low = qp * self.round_trip_eff
            q_out = q_low
        else:
            self.capacity -= q_req
            q_out = qp
        self.output_time += q_out / self.flow_out
        return q_out

    def __repr__(self, scale=5):
        """
        Represents Battery as Cell filled with units of charge
        """
        shell = "["
        r_charges = int(round(self.capacity / scale))
        for i in range(int(round(self.max_capacity / scale))):
            if r_charges < (i - 1):
                shell += " "
            else:
                shell += "|"
        shell += "]"
        cell_charge = shell + \
            "({} %)".format(round(self.get_charge_pct() * 100, 2))
        return cell_charge



b = Battery()
print(b.capacity)

# %%
