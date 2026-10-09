#!/usr/bin/env python3
"""
update_inventory.py
===================
Automatic inventory scanner and README generator for UC3M Aerospace Engineering study sources.

Usage:
    python sources/update_inventory.py

This script scans all subjects under sources/cuatrimestre-1/, compares the existing files
against the official course syllabus checklist, and generates an up-to-date, structured
README.md in each subject folder detailing:
1. Subject metadata and summary statistics
2. Current inventory table (files, sizes, locations)
3. Gap analysis / Pending materials checklist ("Lo que falta")
4. Automated update protocol
"""

import os
import sys
import datetime

# Base path relative to workspace root
WORKSPACE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SOURCES_DIR = os.path.join(WORKSPACE_DIR, "sources")
C1_DIR = os.path.join(SOURCES_DIR, "cuatrimestre-1")

SUBJECT_CONFIGS = {
    "01-fluid-mechanics": {
        "title": "Fluid Mechanics (Mecánica de Fluidos)",
        "code": "251-15334",
        "notebook_id": "3080c1f2-5689-4a39-90c3-091d58f39684",
        "has_labs": True,
        "consolidated_theory": True,
        "exam_structure": ["first-midterm", "second-midterm", "final-exam"],
        "syllabus_units": [
            {
                "id": "unit-01-introductory-remarks",
                "name": "Unit 1: Introductory Remarks & Fluid Properties",
                "theory_expected": ["Slides Ch 1 (in slides_Chapters1-2.pdf)", "Consolidated Notes.pdf Ch 1"],
                "problems_expected": ["Introductory problems / Examples"]
            },
            {
                "id": "unit-02-flow-kinematics",
                "name": "Unit 2: Flow Kinematics",
                "theory_expected": ["Slides Ch 2 (in slides_Chapters1-2.pdf)", "Consolidated Notes.pdf Ch 2"],
                "problems_expected": ["Kinematics Problem Sheet K1–K10"]
            },
            {
                "id": "unit-03-conservation-laws",
                "name": "Unit 3: Conservation Laws (Mass, Momentum, Energy)",
                "theory_expected": ["Slides Ch 3 (Integral Conservation Laws)", "Consolidated Notes.pdf Ch 3"],
                "problems_expected": ["Conservation Laws Problem Sheet CL1–CL22"]
            },
            {
                "id": "unit-04-navier-stokes",
                "name": "Unit 4: The Navier-Stokes Equations (Differential Dynamics)",
                "theory_expected": ["Consolidated Notes.pdf Ch 4"],
                "problems_expected": ["Navier-Stokes Equations Problem Sheet NS1–NS17"]
            },
            {
                "id": "unit-05-hydrostatics",
                "name": "Unit 5: Hydrostatics (Fluid Statics & Manometry)",
                "theory_expected": ["Consolidated Notes.pdf Ch 5"],
                "problems_expected": ["Fluid Statics Problem Sheet (fluid_statics_1 to 10)"]
            },
            {
                "id": "unit-06-dimensional-analysis",
                "name": "Unit 6: Dimensional Analysis & Similitude (Pi Theorem)",
                "theory_expected": ["Consolidated Notes.pdf Ch 6"],
                "problems_expected": ["Dimensional Analysis Problem Sheet DA1–DA14"]
            },
            {
                "id": "unit-07-viscous-flow",
                "name": "Unit 7: Viscous Flows & Boundary Layers",
                "theory_expected": ["Consolidated Notes.pdf Ch 7 & 10"],
                "problems_expected": ["Viscous Flows Problem Sheet VF2–VF20"]
            }
        ],
        "labs_expected": [
            {
                "key": "general-instructions",
                "desc": "General Guidelines & Report Standards (LAB_BLUEPRINT.md in general-instructions/)"
            },
            {
                "key": "lab-1",
                "desc": "Lab Session 1: Venturi Tube & Flow Rate Measurement (Lab_session_1.pdf, measurements, figures & final report in lab-1/)"
            },
            {
                "key": "lab-2",
                "desc": "Lab Session 2: Aerodynamic Drag / Wind Tunnel Practical (lab-2/)"
            },
            {
                "key": "lab-3",
                "desc": "Lab Session 3: Fluid Properties / Viscometry & Manometry (lab-3/)"
            },
            {
                "key": "lab-4",
                "desc": "Lab Session 4: Boundary Layer / Pipe Flow Losses (lab-4/)"
            }
        ],
        "exams_expected": [
            "First Midterm (Parcial 1) past exams and solutions",
            "Second Midterm (Parcial 2) past exams and solutions",
            "Final Exam past papers and official rubrics"
        ]
    },
    "02-aerospace-materials-1": {
        "title": "Aerospace Materials I (Materiales Aeroespaciales I)",
        "code": "251-15333",
        "notebook_id": "9b324478-69e9-482c-813c-5709ec031820",
        "has_labs": True,
        "consolidated_theory": False,
        "exam_structure": ["first-partial", "second-partial", "third-partial", "final-exam"],
        "syllabus_units": [
            {
                "id": "unit-01-atomic-bonding",
                "name": "Topic 1: Bonding in Solids & Material Properties",
                "theory_expected": ["Session 2 T1 Bonding_2025.pdf"],
                "problems_expected": ["Slide 39 Questions (Cuestiones 1-4 de examen)"]
            },
            {
                "id": "unit-02-crystal-structures-defects",
                "name": "Topic 2: Structure of Materials & Crystal Defects",
                "theory_expected": ["Session 3 T2 Structure of Materials I_2025.pdf", "Session 4 T2 Structure of Materials II_2025.pdf"],
                "problems_expected": ["Problems T2_CrystStruct.pdf", "Problems T2 defects.pdf"]
            },
            {
                "id": "unit-03-diffusion-in-solids",
                "name": "Topic 3: Diffusion in Solids & Mass Transport",
                "theory_expected": ["Session 5 T3  Difussion_2025.pdf"],
                "problems_expected": ["Problems T3_Diffusion.pdf"]
            },
            {
                "id": "unit-04-phase-diagrams",
                "name": "Topic 4: Phase Diagrams & Solidification",
                "theory_expected": [
                    "Session 7 T4 Phase diagrams I_2025.pdf",
                    "Session 8 T4 Phase diagrams II.pdf",
                    "Session 9 T4 Phase diagrams III.pdf",
                    "Session 10 T4 Phase diagrams IV.pdf"
                ],
                "problems_expected": [
                    "Problems T4_PhaseDiagrams I.pdf",
                    "Problems T4_PhaseDiagrams II.pdf",
                    "Solution problems Phase diagrams I.pdf",
                    "Solution problems Phase diagrams II.pdf"
                ]
            },
            {
                "id": "unit-05-mechanical-properties",
                "name": "Topic 5: Mechanical Properties & Testing",
                "theory_expected": ["Session 11 T5 Mechanical properties I.pdf", "Session 12 T5 Mechanical properties II.pdf"],
                "problems_expected": ["Problems T5_MechanicalProperties.pdf"]
            },
            {
                "id": "unit-06-electrical-properties",
                "name": "Topic 6: Electrical Properties",
                "theory_expected": ["Session 13 T6 Electrical properties.pdf"],
                "problems_expected": ["Problems T6andT7_Electric and Magnetic Properties.pdf"]
            },
            {
                "id": "unit-07-magnetic-thermal-properties",
                "name": "Topic 7: Magnetic & Thermal Properties",
                "theory_expected": ["Session 15 T7 Magnetic and thermal properties.pdf"],
                "problems_expected": ["Problems T6andT7_Electric and Magnetic Properties.pdf"]
            },
            {
                "id": "unit-08-ceramic-materials",
                "name": "Topic 8: Ceramic Materials & Processing",
                "theory_expected": ["Session 16 T8 Ceramic materials.pdf", "Session 18 T8 Processing of ceramic materials.pdf"],
                "problems_expected": ["Problems T8_CeramicMaterials.pdf"]
            },
            {
                "id": "unit-09-polymers",
                "name": "Topic 9: Polymeric Materials & Processing",
                "theory_expected": ["Session 19 T9 Polymers.pdf", "Session 20 T9 Classification and Polymer Processing.pdf"],
                "problems_expected": ["Problems T9_Polymers.pdf"]
            },
            {
                "id": "unit-10-composite-materials",
                "name": "Topic 10: Composite Materials & Reinforcements",
                "theory_expected": ["Session 21 T10 Composites I.pdf", "Session 22 T10 Composites II.pdf", "Session 23 T10 Composites III.pdf"],
                "problems_expected": ["Problems T10_CompositeMaterials.pdf"]
            },
            {
                "id": "unit-11-adhesives",
                "name": "Topic 11: Structural Adhesives & Joint Design",
                "theory_expected": ["Session 24 T11 Adhesives.pdf"],
                "problems_expected": ["Problems T11 (Adhesive joints & failure mechanisms)"]
            }
        ],
        "labs_expected": [
            {
                "key": "general-instructions",
                "desc": "General Guidelines: Master Guide (LabGuide_AerospaceMaterialsI.pdf) & Intro Presentation in general-instructions/"
            },
            {
                "key": "lab-1",
                "desc": "Lab Session 1: Crystalline Structures (Lab_session_1.pdf in lab-1/)"
            },
            {
                "key": "lab-2",
                "desc": "Lab Session 2: Tensile Test of Metallic Alloys (lab-2/)"
            },
            {
                "key": "lab-3",
                "desc": "Lab Session 3: Composite Materials Fabrication (lab-3/)"
            },
            {
                "key": "lab-4",
                "desc": "Lab Session 4: Identification and Characterization of Polymers (lab-4/)"
            }
        ],
        "exams_expected": [
            "First Partial (Topics 1, 2, 3) - 2022, 2023, Test questions",
            "Second Partial (Topics 4, 5, 6, 7) past exams and solutions",
            "Third Partial (Topics 8, 9, 10, 11) past exams and solutions",
            "Final Exam past papers and solutions"
        ]
    },
    "03-engineering-mechanics": {
        "title": "Engineering Mechanics (Mecánica de Estructuras / Mecánica)",
        "code": "251-15332",
        "notebook_id": "473546c3-3716-4426-b0c4-58de530f91c8",
        "has_labs": True,
        "consolidated_theory": True,
        "exam_structure": ["first-midterm", "second-midterm", "final-exam"],
        "syllabus_units": [
            {
                "id": "unit-01-particle-kinematics",
                "name": "Part I - Unit 1: Point Particle Kinematics",
                "theory_expected": ["00.pdf", "01_-_Point_particle_kinematics.pdf", "Consolidated Notes.pdf Ch 1-2"],
                "problems_expected": ["Problems.pdf Problems 1 to 14"]
            },
            {
                "id": "unit-02-particle-dynamics",
                "name": "Part I - Unit 2: Point Particle Dynamics",
                "theory_expected": ["02.PointParticleDynamics.pdf", "Consolidated Notes.pdf Ch 4"],
                "problems_expected": ["Problems.pdf Problems 15 to 25"]
            },
            {
                "id": "unit-03-constraints-reactions",
                "name": "Part I - Unit 3: Constraints & Reactions",
                "theory_expected": ["03_-_Constraints.pdf", "Consolidated Notes.pdf Ch 2.7 & 13"],
                "problems_expected": ["Problems.pdf Problems 26 to 34"]
            },
            {
                "id": "unit-04-angular-momentum-central-forces",
                "name": "Part I - Unit 4: Angular Momentum & Central Forces",
                "theory_expected": ["04_-_Angular_momentum.pdf", "Consolidated Notes.pdf Ch 5"],
                "problems_expected": ["Problems.pdf Problems 35 to 42"]
            },
            {
                "id": "unit-05-relative-motion",
                "name": "Part I - Unit 5: Relative Motion",
                "theory_expected": ["05_-_Relative_motion.pdf", "Consolidated Notes.pdf Ch 3"],
                "problems_expected": ["Problems.pdf Problems 43 to 51"]
            },
            {
                "id": "unit-06-systems-of-particles",
                "name": "Part II - Unit 6: Systems of Particles & Center of Mass",
                "theory_expected": ["Slides Unit 6", "Consolidated Notes.pdf Ch 6"],
                "problems_expected": ["Problems.pdf Part II Systems Problems"]
            },
            {
                "id": "unit-07-geometry-of-masses",
                "name": "Part II - Unit 7: Geometry of Masses & Inertia Tensor",
                "theory_expected": ["Slides Unit 7", "Consolidated Notes.pdf Ch 10"],
                "problems_expected": ["Problems.pdf Part II Inertia Problems"]
            },
            {
                "id": "unit-08-rigid-body-kinematics",
                "name": "Part II - Unit 8: Rigid Body Kinematics & General Dynamics",
                "theory_expected": ["Slides Unit 8", "Consolidated Notes.pdf Ch 11-12"],
                "problems_expected": ["Problems.pdf Part II Rigid Body Problems"]
            },
            {
                "id": "unit-09-gyroscopic-motion",
                "name": "Part II - Unit 9: Planar Dynamics & Gyroscopic Motion",
                "theory_expected": ["Slides Unit 9", "Consolidated Notes.pdf Ch 14-15"],
                "problems_expected": ["Problems.pdf Gyroscope Problems"]
            },
            {
                "id": "unit-10-aerodynamic-forces",
                "name": "Part III - Unit 10: Airplane Definitions & Aerodynamic Forces",
                "theory_expected": ["Slides Unit 10", "Consolidated Notes.pdf Ch 16"],
                "problems_expected": ["Flight Mechanics Introductory Problems"]
            },
            {
                "id": "unit-11-aircraft-equations",
                "name": "Part III - Unit 11: Aircraft Equations of Motion",
                "theory_expected": ["Slides Unit 11", "Consolidated Notes.pdf Ch 16.3"],
                "problems_expected": ["Aircraft Trajectory & Balance Problems"]
            },
            {
                "id": "unit-12-longitudinal-equilibrium",
                "name": "Part III - Unit 12: Longitudinal Equilibrium & Performance",
                "theory_expected": ["Slides Unit 12", "Consolidated Notes.pdf Ch 16.4"],
                "problems_expected": ["Longitudinal Stability & Performance Problems"]
            }
        ],
        "labs_expected": [
            {
                "key": "general-instructions",
                "desc": "General Guidelines & Plotting Standards: mechanics_labs.pdf in general-instructions/"
            },
            {
                "key": "Lab1-Ismael",
                "desc": "Lab Session 1: Particle Connected to a Spool (Analytical vs numerical MATLAB simulation & Overleaf report in Lab1-Ismael/)"
            },
            {
                "key": "lab-2",
                "desc": "Lab Session 2: Particle on Oscillating Loop (lab-2/)"
            },
            {
                "key": "lab-3",
                "desc": "Lab Session 3: Compound Double Pendulum - Experimental Testing (lab-3/)"
            },
            {
                "key": "lab-4",
                "desc": "Lab Session 4: Compound Double Pendulum - Numerical Integration (lab-4/)"
            }
        ],
        "exams_expected": [
            "First Midterm (Part I Particle Mechanics) past exams and solutions",
            "Second Midterm (Part II Rigid Body Mechanics) past exams and solutions",
            "Final Exam past papers and solutions"
        ]
    },
    "04-advanced-maths": {
        "title": "Advanced Mathematics (Matemáticas Avanzadas)",
        "code": "251-15331",
        "notebook_id": "c27033c3-5a64-403f-a517-5847831aabcb",
        "has_labs": False,
        "consolidated_theory": False,
        "exam_structure": ["first-midterm", "second-midterm", "final-exam"],
        "syllabus_units": [
            {
                "id": "unit-01-introduction-ode-modeling",
                "name": "Unit 1: Introduction to ODEs & Mathematical Modeling",
                "theory_expected": ["BookODE's.pdf (Ch 1)"],
                "problems_expected": ["ProblemsCh1.pdf"]
            },
            {
                "id": "unit-02-first-order-odes",
                "name": "Unit 2: First-Order ODEs & Qualitative Dynamics",
                "theory_expected": ["BookODE's.pdf (Ch 2)", "Lecture notes on integrating factors & exact equations"],
                "problems_expected": ["ProblemsCh2.pdf"]
            },
            {
                "id": "unit-03-second-order-linear-odes",
                "name": "Unit 3: Second-Order Linear ODEs & Vibrations",
                "theory_expected": ["BookODE's.pdf (Ch 3)", "Lecture notes on Wronskian & variation of parameters"],
                "problems_expected": ["ProblemsCh3.pdf", "probls_ch3_2627.pdf"]
            },
            {
                "id": "unit-04-systems-of-odes",
                "name": "Unit 4: Linear Systems of ODEs & Phase Plane",
                "theory_expected": ["definition_linear_ODE.pdf", "BookODE's.pdf (Ch 4)"],
                "problems_expected": ["Systems of ODEs Problem Sheet (Ch 4)"]
            },
            {
                "id": "unit-05-fourier-series-pdes",
                "name": "Unit 5: Fourier Series & Boundary Value Problems",
                "theory_expected": ["BookPDE's.pdf (Ch 1-2)"],
                "problems_expected": ["Fourier Series Problem Sheet (Ch 5)"]
            },
            {
                "id": "unit-06-classical-pdes",
                "name": "Unit 6: Classical PDEs (Heat, Wave & Laplace Equations)",
                "theory_expected": ["BookPDE's.pdf (Ch 3-5)"],
                "problems_expected": ["PDE Separation of Variables Problem Sheet (Ch 6)"]
            }
        ],
        "labs_expected": [],
        "exams_expected": [
            "First Midterm (ODEs Ch 1-3) past exams and solutions",
            "Second Midterm (Systems & Fourier) past exams and solutions",
            "Final Exam past papers and solutions"
        ]
    },
    "05-business-management": {
        "title": "Business Management (Gestión de Empresas)",
        "code": "251-15335",
        "notebook_id": "e691ea81-0acf-4032-98d1-b9e5a7b93d70",
        "has_labs": False,
        "consolidated_theory": False,
        "exam_structure": ["first-midterm", "second-midterm", "final-exam"],
        "syllabus_units": [
            {
                "id": "unit-01-the-firm-types-objectives",
                "name": "Unit 1: The Firm — Types, Objectives & Governance",
                "theory_expected": ["Topic 1_The Firm_Types  Objectives.pdf"],
                "problems_expected": ["W1 Pr_Elevator Pitch  Governance.pdf"]
            },
            {
                "id": "unit-02-value-creation-environment",
                "name": "Unit 2: Value Creation, Environment & Strategy",
                "theory_expected": ["Topic 2_ Value creation.pdf"],
                "problems_expected": ["W2 Practice_2_Business Environment.pdf", "W3 Practice_3_Int_Analysis_Strategy_Resources.pdf"]
            },
            {
                "id": "unit-03-financial-management-statements",
                "name": "Unit 3: Financial Management & Accounting Statements",
                "theory_expected": ["Topic 3_Financial Management (I).pdf"],
                "problems_expected": ["T3_Financial Statements_EXERCISES.pdf", "T3_Additional_EXERCISES.pdf"]
            },
            {
                "id": "unit-04-operations-management",
                "name": "Unit 4: Production & Operations Management",
                "theory_expected": ["Topic 4 Theory Slides (Production, Costs, Capacity)"],
                "problems_expected": ["Operations & Break-even Exercises"]
            },
            {
                "id": "unit-05-marketing-strategy",
                "name": "Unit 5: Marketing & Commercial Strategy",
                "theory_expected": ["Topic 5 Theory Slides (Marketing Mix, Market Analysis)"],
                "problems_expected": ["Marketing Case Studies"]
            },
            {
                "id": "unit-06-business-plan",
                "name": "Unit 6: Business Plan Formulation",
                "theory_expected": [
                    "BUSINESS PLAN_guide_26_27.pdf",
                    "Engineers  Managing_Business Plan_26-27 W1.pdf",
                    "how-to-write-a-business-plan.pdf"
                ],
                "problems_expected": ["Business Plan Milestones & Rubrics"]
            }
        ],
        "labs_expected": [],
        "exams_expected": [
            "Midterm Exam past papers and test questions",
            "Final Exam past papers and business case solutions"
        ]
    }
}


def format_size(bytes_num):
    for unit in ['B', 'KB', 'MB', 'GB']:
        if bytes_num < 1024.0:
            return f"{bytes_num:3.1f} {unit}"
        bytes_num /= 1024.0
    return f"{bytes_num:.1f} TB"


def scan_subject_files(subj_path):
    all_files = []
    for root, dirs, files in os.walk(subj_path):
        for f in files:
            if f.lower() == "readme.md":
                continue
            full_p = os.path.join(root, f)
            rel_p = os.path.relpath(full_p, subj_path)
            size = os.path.getsize(full_p)
            all_files.append({
                "name": f,
                "rel_path": rel_p.replace("\\", "/"),
                "size_bytes": size,
                "size_fmt": format_size(size)
            })
    return all_files


def generate_subject_readme(subj_key, config):
    subj_path = os.path.join(C1_DIR, subj_key)
    if not os.path.isdir(subj_path):
        return

    files = scan_subject_files(subj_path)

    # Categorize files
    theory_files = [f for f in files if "teoria" in f["rel_path"] or "slides" in f["rel_path"]]
    problem_files = [f for f in files if "problemas" in f["rel_path"]]
    lab_files = [f for f in files if "laboratorios" in f["rel_path"]]
    exam_files = [f for f in files if "examenes" in f["rel_path"]]
    schedule_files = [f for f in files if "schedule" in f["rel_path"]]

    total_files = len(files)
    total_size = sum(f["size_bytes"] for f in files)

    now_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

    md = []
    md.append(f"# 📚 {config['title']}")
    md.append("")
    md.append(f"> **Course Code:** `{config['code']}` | **Degree:** BSc in Aerospace Engineering (UC3M) | **Term:** 2nd Year, 1st Term  ")
    md.append(f"> **NotebookLM ID:** `{config['notebook_id']}`  ")
    md.append(f"> **Portal Web:** `subjects/{subj_key}/` | **Obsidian Vault:** `vault/{subj_key}/`  ")
    md.append(f"> **Last Synchronized:** `{now_str}` | **Total Official Files:** `{total_files}` ({format_size(total_size)})")
    md.append("")
    md.append("---")
    md.append("")

    # Summary Badges / Statistics
    md.append("## 📊 Summary of Resources")
    md.append("")
    md.append("| Category | File Count | Status | Notes |")
    md.append("| :--- | :---: | :---: | :--- |")
    md.append(f"| 📖 **Theory & Slides** | `{len(theory_files)}` | {'🟢 Active' if theory_files else '🔴 Pending'} | Consolidated Notes & Session Slides |")
    md.append(f"| ✏️ **Problem Sheets & Solutions** | `{len(problem_files)}` | {'🟢 Active' if problem_files else '🔴 Pending'} | Official problem sets & step-by-step solutions |")
    if config["has_labs"]:
        md.append(f"| 🔬 **Laboratory Practicals** | `{len(lab_files)}` | {'🟢 Active' if lab_files else '🔴 Pending'} | Structured into general-instructions/ & lab-1..4/ |")
    md.append(f"| 📝 **Official Exams** | `{len(exam_files)}` | {'🟢 Active' if exam_files else '🟡 Incomplete'} | Partial midterms & final exams |")
    md.append(f"| 📅 **Course Schedule** | `{len(schedule_files)}` | {'🟢 Available' if schedule_files else '🔴 Pending'} | Weekly lecture & evaluation calendar |")
    md.append("")
    md.append("---")
    md.append("")

    # Section 1: Detailed Available Inventory
    md.append("## 📦 Detailed Resource Inventory (Present Files)")
    md.append("")
    if not files:
        md.append("*No files have been uploaded to this subject yet.*")
    else:
        md.append("| # | File Name | Category / Subfolder | Size | File Path |")
        md.append("| :---: | :--- | :--- | :---: | :--- |")
        for idx, f in enumerate(sorted(files, key=lambda x: x["rel_path"]), 1):
            category = "Other"
            rp = f["rel_path"].lower()
            if "schedule" in rp:
                category = "📅 Schedule"
            elif "teoria" in rp:
                category = "📖 Theory"
            elif "slides" in rp:
                category = "🖥️ Slides"
            elif "problemas" in rp:
                category = "✏️ Problems"
            elif "laboratorios/general-instructions" in rp:
                category = "🔬 Lab (General Instructions)"
            elif "laboratorios/lab-1" in rp:
                category = "🔬 Lab 1"
            elif "laboratorios/lab-2" in rp:
                category = "🔬 Lab 2"
            elif "laboratorios/lab-3" in rp:
                category = "🔬 Lab 3"
            elif "laboratorios/lab-4" in rp:
                category = "🔬 Lab 4"
            elif "laboratorios" in rp:
                category = "🔬 Lab"
            elif "examenes" in rp:
                category = "📝 Exam"
            md.append(f"| {idx} | `{f['name']}` | {category} | {f['size_fmt']} | `{f['rel_path']}` |")
    md.append("")
    md.append("---")
    md.append("")

    # Section 2: Gap Analysis & Missing Materials Checklist ("Lo que falta")
    md.append("## 📋 Gap Analysis & Missing Materials Tracker (\"Lo que Falta\")")
    md.append("")
    md.append("This checklist tracks all academic materials required according to the official UC3M syllabus. It identifies existing items and highlights missing documents that should be uploaded when published.")
    md.append("")

    # 1. Schedule
    has_sched = len(schedule_files) > 0
    md.append("### 1. Course Schedule & Organization")
    md.append(f"- [{'x' if has_sched else ' '}] **Official Syllabus & Calendar (`schedule/`):** " +
              (f"Present (`{schedule_files[0]['name']}`)" if has_sched else "MISSING. Upload official PDF calendar."))
    md.append("")

    # 2. Theory & Problems by Unit
    md.append("### 2. Syllabus Units & Weekly Topics")
    md.append("")
    for unit in config["syllabus_units"]:
        u_id = unit["id"]
        u_name = unit["name"]
        md.append(f"#### {u_name} (`{u_id}/`)")
        
        # Check theory
        md.append("  * **Theory / Slides:**")
        for item in unit["theory_expected"]:
            found = any(item.lower() in f["name"].lower() or any(word in f["name"].lower() for word in item.lower().split() if len(word) > 4) for f in files)
            # Check if consolidated notes covers it
            if config["consolidated_theory"] and any(f["name"] == "Notes.pdf" for f in files):
                found = True
            mark = "x" if found else " "
            md.append(f"    - [{mark}] {item}")

        # Check problems
        md.append("  * **Problems & Solutions:**")
        for item in unit["problems_expected"]:
            found = False
            for f in files:
                if "problemas" in f["rel_path"]:
                    if u_id in f["rel_path"]:
                        found = True
                        break
            if "problems.pdf" in [f["name"].lower() for f in files]:
                found = True
            mark = "x" if found else " "
            md.append(f"    - [{mark}] {item}")
        md.append("")

    # 3. Laboratory Practicals (if applicable)
    if config["has_labs"]:
        md.append("### 3. Laboratory Practicals (`laboratorios/`)")
        for lab_item in config["labs_expected"]:
            key = lab_item["key"]
            desc = lab_item["desc"]
            # Check if there are files in that lab folder
            matching_files = [f for f in lab_files if f"laboratorios/{key}" in f["rel_path"]]
            found = len(matching_files) > 0
            mark = "x" if found else " "
            md.append(f"- [{mark}] **`{key}/`**: {desc}")
        md.append("")

    # 4. Official Exams
    md.append("### 4. Official Exams & Tests (`examenes/`)")
    for ex_desc in config["exams_expected"]:
        found = False
        for f in exam_files:
            if "first" in ex_desc.lower() or "parcial 1" in ex_desc.lower() or "test 1" in ex_desc.lower():
                if "first" in f["rel_path"].lower() or "1st" in f["rel_path"].lower():
                    found = True
            elif "second" in ex_desc.lower() or "parcial 2" in ex_desc.lower() or "test 2" in ex_desc.lower():
                if "second" in f["rel_path"].lower() or "2nd" in f["rel_path"].lower():
                    found = True
            elif "third" in ex_desc.lower() or "test 3" in ex_desc.lower():
                if "third" in f["rel_path"].lower() or "3rd" in f["rel_path"].lower():
                    found = True
            elif "final" in ex_desc.lower():
                if "final" in f["rel_path"].lower():
                    found = True
        mark = "x" if found else " "
        md.append(f"- [{mark}] {ex_desc}")
    md.append("")
    md.append("---")
    md.append("")

    # Section 3: Update Protocol & Automation Instructions
    md.append("## 🔄 Automated Update Protocol (\"Cómo Actualizar\")")
    md.append("")
    md.append("Whenever you upload new files to this subject or to `sources/`, follow this simple process to keep the inventory and checklists synchronized:")
    md.append("")
    md.append("1. **Drop New Files into the Correct Subfolder:**")
    md.append("   - **Theory / Lecture Slides:** Place in `unit-XX-<topic>/teoria/` (or `slides/` for consolidated subjects).")
    md.append("   - **Problem Sheets / Solutions:** Place in `unit-XX-<topic>/problemas/`.")
    md.append("   - **Exams:** Place in `examenes/<first-partial | second-partial | third-partial | final-exam>/`.")
    if config["has_labs"]:
        md.append("   - **Laboratory Materials:**")
        md.append("     - General guides and policies: `laboratorios/general-instructions/`")
        md.append("     - Specific lab sessions: `laboratorios/lab-1/`, `laboratorios/lab-2/`, `laboratorios/lab-3/`, `laboratorios/lab-4/`")
    md.append("   - **Schedule / Calendar:** Place in `schedule/`.")
    md.append("")
    md.append("2. **Run the Automatic Synchronizer:**")
    md.append("   Execute the update script from the project root in PowerShell or terminal:")
    md.append("   ```bash")
    md.append("   python sources/update_inventory.py")
    md.append("   ```")
    md.append("   *This will automatically scan all files, update the inventory tables, recalculate file sizes, and refresh the \"Lo que Falta\" checklists across all subjects.*")
    md.append("")
    md.append("3. **Downstream Propagation (Obsidian & Web):**")
    md.append("   After updating sources, the pedagogical subagents (`aerospace_pedagogue` and `problem_step_mentor`) reference this README to ingest new topics into the Obsidian vault (`vault/`) and develop corresponding web study modules (`subjects/`).")
    md.append("")

    readme_path = os.path.join(subj_path, "README.md")
    with open(readme_path, "w", encoding="utf-8") as out:
        out.write("\n".join(md) + "\n")
    print(f"Generated: {readme_path} ({len(files)} files recorded)")


def generate_all():
    print("=== Scanning and Updating All Subject Inventories ===")
    for subj_key, config in SUBJECT_CONFIGS.items():
        generate_subject_readme(subj_key, config)
    print("=== All README trackers successfully generated! ===")


if __name__ == "__main__":
    generate_all()
