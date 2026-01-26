from pyuvm import uvm_sequence
from .cl_rst_seq_item import cl_rst_seq_item


class cl_rst_base_seq(uvm_sequence):

    def __init__(self, name="cl_rst_base_seq"):
        super().__init__(name)
        self.seq_item: cl_rst_seq_item | None = None

    async def body(self):
        await super().body()
        if self.seq_item is None:
            self.seq_item = cl_rst_seq_item.create("seq_item")
        await self.start_item(self.seq_item)
        await self.finish_item(self.seq_item)


class cl_rst_apply_seq(cl_rst_base_seq):

    def __init__(self, name="cl_rst_apply_seq"):
        super().__init__(name)

    async def body(self):
        if self.seq_item is None:
            self.seq_item = cl_rst_seq_item("seq_item")
        self.seq_item.parent_sequnce = "apply"
        await super().body()


class cl_rst_release_seq(cl_rst_base_seq):

    def __init__(self, name="cl_rst_release_seq"):
        super().__init__(name)

    async def body(self):
        if self.seq_item is None:
            self.seq_item = cl_rst_seq_item("seq_item")
        self.seq_item.parent_sequnce = "release"
        await super().body()
