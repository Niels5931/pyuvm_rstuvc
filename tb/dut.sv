// Simple DUT with reset input for testing the reset driver
module dut (
    input logic clk,
    input logic rst_n
);

    // Simple counter to verify reset is working
    logic [7:0] counter;

    always_ff @(posedge clk or negedge rst_n) begin
        if (!rst_n)
            counter <= 8'h0;
        else
            counter <= counter + 1;
    end

endmodule
