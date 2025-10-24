import java.util.ArrayList;
import java.util.Date;
import java.util.List;

public class Main {
    // --- Patient Class ---
    static class Patient {
        int patientID;
        String name;
        Date dateOfBirth;
        String patientType;

        public Patient(int patientID, String name, Date dateOfBirth, String patientType) {
            this.patientID = patientID;
            this.name = name;
            this.dateOfBirth = dateOfBirth;
            this.patientType = patientType;
        }

        public void updatePatient(String name, Date dob) {
            this.name = name;
            this.dateOfBirth = dob;
        }

        public String getPatientInfo() {
            return "ID: " + patientID + ", Name: " + name + ", DOB: " + dateOfBirth + ", Type: " + patientType;
        }
    }

    // --- HosRoom Class ---
    static class HosRoom {
        int roomNumber;
        String roomType;
        double roomFee;
        boolean occupied = false;

        public HosRoom(int roomNumber, String roomType, double roomFee) {
            this.roomNumber = roomNumber;
            this.roomType = roomType;
            this.roomFee = roomFee;
        }

        public void assignPatient(Patient p) {
            occupied = true;
            // Assuming p.name is accessible here; if Patient fields were private, a getName() method would be needed.
            System.out.println("Room " + roomNumber + " assigned to patient " + p.name);
        }

        public void releasePatient() {
            occupied = false;
            System.out.println("Room " + roomNumber + " is now available.");
        }

        public boolean isOccupied() {
            return occupied;
        }
    }

    // --- ResPatient Class ---
    static class ResPatient extends Patient {
        int roomPatient;

        public ResPatient(int patientID, String name, Date dob, int roomPatient) {
            super(patientID, name, dob, "Resident");
            this.roomPatient = roomPatient;
        }

        public void assignRoom(HosRoom room) {
            this.roomPatient = room.roomNumber;
            room.assignPatient(this);
        }
    }

    // --- OutPatient Class ---
    static class OutPatient extends Patient {
        public OutPatient(int patientID, String name, Date dob) {
            super(patientID, name, dob, "Outpatient");
        }

        public void discharge() {
            System.out.println(name + " has been discharged.");
        }
    }

    // --- HosFlow Class ---
    static class HosFlow {
        List<Patient> patients = new ArrayList<>();
        List<HosRoom> rooms = new ArrayList<>();

        public void addPatient(Patient p) {
            patients.add(p);
        }

        public void updatePatient(int id, String newName, Date newDob) {
            for (Patient p : patients) {
                if (p.patientID == id) {
                    p.updatePatient(newName, newDob);
                    System.out.println("Updated patient " + id);
                    return;
                }
            }
            System.out.println("Patient not found.");
        }

        public Patient searchPatient(int id) {
            for (Patient p : patients) {
                if (p.patientID == id) {
                    return p;
                }
            }
            return null;
        }

        public void viewPatient(int id) {
            Patient p = searchPatient(id);
            if (p != null) {
                System.out.println(p.getPatientInfo());
            } else {
                System.out.println("Patient not found.");
            }
        }

        public void viewRstat(int roomNumber) {
            for (HosRoom r : rooms) {
                if (r.roomNumber == roomNumber) {
                    System.out.println("Room " + r.roomNumber + " occupied: " + r.isOccupied());
                    return;
                }
            }
            System.out.println("Room not found.");
        }
    }

    // --- Main Method ---
    public static void main(String[] args) {
        HosFlow system = new HosFlow();

        HosRoom room101 = new HosRoom(101, "Private", 1500.0);
        HosRoom room102 = new HosRoom(102, "Semi-Private", 1000.0);
        system.rooms.add(room101);
        system.rooms.add(room102);

        ResPatient rp = new ResPatient(1, "Juan Dela Cruz", new Date(), 0); // Initial room ID set to 0
        OutPatient op = new OutPatient(2, "Maria Clara", new Date());
        
        system.addPatient(rp);
        system.addPatient(op);

        rp.assignRoom(room101);

        system.viewPatient(1);
        system.viewPatient(2);

        system.viewRstat(101);
        system.viewRstat(102);

        op.discharge();

        room101.releasePatient();
        system.viewRstat(101);
    }
}
