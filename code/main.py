import datetime
import tkinter as tk
from tkinter import messagebox


def show_calendar(squat, bench, deadlift):
    # Create a new frame for the calendar view
    calendar_frame = tk.Frame(root)
    calendar_frame.pack(pady=10, fill="both", expand=True)

    current_year = datetime.date.today().year
    month_names = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]

    # Title label for the calendar view (spanning 3 columns)
    title_label = tk.Label(
        calendar_frame,
        text=f"Workout Plan for {current_year}",
        font=("Helvetica", 16, "bold"),
    )
    title_label.grid(row=0, column=0, columnspan=3, pady=10)

    # Colors for the different rows in the table
    day_header_bg = "#d0e1f9"  # Light blue
    warmup_bg = "#f9f3d0"  # Light yellow
    main_lift_bg = "#f9d0d0"  # Light pink
    aux_lift_bg = "#d0f9d8"  # Light green
    accessories_bg = "#d0d0f9"  # Light purple
    finisher_bg = "#f0f0f0"  # Light grey

    # Create a 4x3 grid for the 12 months (starting at grid row 1)
    for i, month in enumerate(month_names):
        row = (i // 3) + 1  # offset by 1 due to title row
        col = i % 3

        # Create a frame for the month cell with border
        month_frame = tk.Frame(calendar_frame, bd=1, relief="solid", padx=5, pady=5)
        month_frame.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

        # Month header inside the cell
        header_label = tk.Label(
            month_frame, text=f"{month} {current_year}", font=("Helvetica", 12, "bold")
        )
        header_label.grid(row=0, column=0, columnspan=3, pady=(0, 5))

        # Row 1: Table header for days (Monday, Wednesday, Friday)
        days = ["Monday", "Wednesday", "Friday"]
        for j, day in enumerate(days):
            day_label = tk.Label(
                month_frame,
                text=day,
                font=("Helvetica", 10, "bold"),
                bd=1,
                relief="solid",
                padx=3,
                pady=3,
                bg=day_header_bg,
            )
            day_label.grid(row=1, column=j, sticky="nsew", padx=1, pady=1)

        # Row 2: Shared warm-up row (spanning 3 columns)
        warmup_label = tk.Label(
            month_frame,
            text="10 min of cardio + 10 min of stretching",
            font=("Helvetica", 10, "italic"),
            bd=1,
            relief="solid",
            padx=3,
            pady=3,
            bg=warmup_bg,
        )
        warmup_label.grid(row=2, column=0, columnspan=3, sticky="nsew", padx=1, pady=1)

        # Compute monthly increments: each month adds 5 kg per lift.
        increment = i * 5
        month_squat = squat + increment
        month_bench = bench + increment
        month_deadlift = deadlift + increment

        # Row 3: Main lift row
        main_lifts = [
            f"Squat @ {month_squat} kg",
            f"Bench @ {month_bench} kg",
            f"Deadlift @ {month_deadlift} kg",
        ]
        for j, lift in enumerate(main_lifts):
            lift_label = tk.Label(
                month_frame,
                text=lift,
                font=("Helvetica", 10, "bold"),
                bd=1,
                relief="solid",
                padx=3,
                pady=3,
                bg=main_lift_bg,
            )
            lift_label.grid(row=3, column=j, sticky="nsew", padx=1, pady=1)

        # Row 4: Auxiliary lift row
        aux_lifts = ["Narrow Bench Press 4x8", "Deadlift 4x8", "Hack Squat 4x8"]
        for j, aux in enumerate(aux_lifts):
            aux_label = tk.Label(
                month_frame,
                text=aux,
                font=("Helvetica", 10),
                bd=1,
                relief="solid",
                padx=3,
                pady=3,
                bg=aux_lift_bg,
            )
            aux_label.grid(row=4, column=j, sticky="nsew", padx=1, pady=1)

        # Row 5: Accessories row
        accessories = [
            "Pull-ups, Rows, Lateral Raises\n3xAMRAP",
            "Assisted Squats, Leg Extensions,\nBulgarian Split Squats\n3xAMRAP",
            "Dips, Dumbbell Shoulder Presses,\nBiceps Curls\n3xAMRAP",
        ]
        for j, acc in enumerate(accessories):
            acc_label = tk.Label(
                month_frame,
                text=acc,
                font=("Helvetica", 10),
                bd=1,
                relief="solid",
                padx=3,
                pady=3,
                bg=accessories_bg,
            )
            acc_label.grid(row=5, column=j, sticky="nsew", padx=1, pady=1)

        # Row 6: Final shared row (spanning 3 columns)
        finisher_label = tk.Label(
            month_frame,
            text="3xAMRAP Kettlebell Side Bends",
            font=("Helvetica", 10, "italic"),
            bd=1,
            relief="solid",
            padx=3,
            pady=3,
            bg=finisher_bg,
        )
        finisher_label.grid(
            row=6, column=0, columnspan=3, sticky="nsew", padx=1, pady=1
        )

        # Configure grid weights in each month frame for even cell expansion
        for r in range(1, 7):
            month_frame.rowconfigure(r, weight=1)
        for j in range(3):
            month_frame.columnconfigure(j, weight=1)

    # Configure grid weights for the main calendar_frame
    for col in range(3):
        calendar_frame.columnconfigure(col, weight=1)
    for r in range(1, 5):  # rows for the 4 month-rows (excluding title)
        calendar_frame.rowconfigure(r, weight=1)


def on_ok():
    # Retrieve input values and convert them to floats.
    try:
        squat = float(squat_entry.get())
        bench = float(bench_entry.get())
        deadlift = float(deadlift_entry.get())
    except ValueError:
        messagebox.showwarning(
            "Input Error", "Please enter valid numbers for all fields!"
        )
        return

    # Hide the input frame (first screen)
    input_frame.pack_forget()

    # Show the calendar view with the computed workout plan.
    show_calendar(squat, bench, deadlift)


# Initialize the main window.
root = tk.Tk()
root.title("Powerlifting App")
root.geometry("800x800")

# --- Input Frame ---
input_frame = tk.Frame(root)
input_frame.pack(pady=20)

instruction_label = tk.Label(
    input_frame, text="Enter your initial lift values (kg):", font=("Helvetica", 14)
)
instruction_label.pack(pady=10)

# Squat input field
squat_label = tk.Label(input_frame, text="Squat (kg):", font=("Helvetica", 12))
squat_label.pack()
squat_entry = tk.Entry(input_frame, font=("Helvetica", 12))
squat_entry.pack(pady=5)

# Bench Press input field
bench_label = tk.Label(input_frame, text="Bench Press (kg):", font=("Helvetica", 12))
bench_label.pack()
bench_entry = tk.Entry(input_frame, font=("Helvetica", 12))
bench_entry.pack(pady=5)

# Deadlift input field
deadlift_label = tk.Label(input_frame, text="Deadlift (kg):", font=("Helvetica", 12))
deadlift_label.pack()
deadlift_entry = tk.Entry(input_frame, font=("Helvetica", 12))
deadlift_entry.pack(pady=5)

# OK Button to trigger the calendar view.
ok_button = tk.Button(input_frame, text="OK", font=("Helvetica", 12), command=on_ok)
ok_button.pack(pady=20)

# Start the Tkinter event loop.
root.mainloop()
