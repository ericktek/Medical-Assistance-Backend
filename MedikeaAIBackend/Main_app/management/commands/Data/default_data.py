metadata = {
  "provisional_experts_levels": [
    {
      "name": "Specialist",
      "Level": ["A", "B", "C", "D", "S"]
    },
    {
      "name": "Medical Officer (MO)",
      "Level": ["A", "B", "C", "D"]
    },
    {
      "name": "Medical Assistant Officer (MAO)",
      "Level": ["A", "B", "C"]
    },
    {
      "name": "Clinical Officer (CO)",
      "Level": ["A", "B"]
    },
    {
      "name": "Assistant Clinical Officer (ACO)",
      "Level": ["A"]
    }
  ],
  "service_provision_level": [
    {
      "name": "Tertiary Hospital",
      "Level": ["A", "B", "C", "D", "S"]
    },
    {
      "name": "Regional Referral Hospital",
      "Level": ["A", "B", "C", "D"]
    },
    {
      "name": "District Hospital",
      "Level": ["A", "B", "C"]
    },
    {
      "name": "Health Centre",
      "Level": ["A", "B"]
    },
    {
      "name": "Dispensary",
      "Level": ["A"]
    }
  ],
  "diseases": [
    {
      "name": "Iron Deficiency Anaemia",
      "description": "A lack of iron in the body (mainly due to nutritional deficiency, chronic blood loss, malabsorption and hookworm infestations and increased demand such as during pregnancy).",
      "clinical_presentation": "fatigue, palpitation, dizziness, glossitis, koilonychias (spoon shaped nails) and pica",
      "investigations": [
        "Full blood picture (FBP)",
        "Peripheral smear",
        "Iron studies- serum iron levels, total iron binding capacity, serum ferritin",
        "Stool analysis for hookworm ova and occult blood. If stool for occult blood is positive, do Oesophagoduodenoscopy (OGD) to confirm upper gastrointestinal bleeding"
      ],
      "treatments": [
        {
          "Non-Pharmacological Treatment": [
            {
              "To prevent iron deficiency": [
                "Eat a variety of iron rich foods like meat, eggs, legumes (dried beans, lentils, peas), spinach and dark green leafy vegetables, iron fortified breads and cereals, nuts and seeds."
              ],
              "To help in iron absorption from diet": [
                "Avoid drinking tea/coffee with meals",
                "Increase intake of vitamin C rich foods (e.g. citrus fruit, broccoli, cauliflower, guavas, tomatoes, bell peppers and strawberries) with meals to maintain iron in its reduced state"
              ]
            }
          ]
        },
        {
          "Pharmacological Treatment": [
            {
              "age/Group": "Adults",
              "drugs": [
                {
                  "class": "A",
                  "name": "ferrous sulfate",
                  "weight": "200mg",
                  "frequency": "8hourly",
                  "total_time_for_usage": "3 months"
                }
              ]
            },
            {
              "age/Group": "Children",
              "drugs": [
                {
                  "class": "A",
                  "name": "ferrous sulphate (PO)",
                  "weight": "5mg/kg",
                  "frequency": "8hourly",
                  "total_time_for_usage": "3 months after the normal hemoglobin has been achieved"
                }
              ]
            },
            {
              "age/Group": "Any",
              "drugs": [
                {
                  "class": "A",
                  "name": "Blood transfusion",
                  "weight": "",
                  "frequency": "",
                  "total_time_for_usage": "",
                  "conditions": "only indicated if anaemia is life threatening; e.g anaemia in failure, hypoxia."
                },
                {
                  "class": "A",
                  "name": "Iron sucrose (IV)",
                  "weight": "200mg in 100ml 0.9% sodium chloride",
                  "frequency": "running for 15 minutes once a day three times a week for 2 weeks",
                  "total_time_for_usage": "number of 100mg ampoules for Hb increase"
                }
              ]
            }
          ]
        }
      ],
      "notes": []
    },
    {
      "name": "Megaloblastic Anemia",
      "description": "This is a condition whereby the bone marrow usually produces large, structurally abnormal, immature red blood cells (megaloblasts) often due to inadequate intake or malabsorption of vitamin B12 or folate.",
      "clinical_presentation": "Pallor, depression, hair loss, pins and needles, numbness in hands or feet, tremors and palsies, mildly jaundiced (lemon yellow tint), beefy tongue, darkening of palms and ataxic gait.",
      "investigations": [
        "FBC-Low Hb, sometime pancytopenia, raised mcv but maybe low or normal if coexisting with iron deficiency (combined deficiency anaemia)",
        "Peripheral smear",
        "Serum vitamin B12",
        "Serum folate level",
        "TSH",
        "Reticulocyte count",
        "Bone marrow aspiration may be indicated"
      ],
      "treatments": [
        {
          "Pharmacological Treatment": [
            {
              "reason": "Vitamin (B12 deficiency anaemia) and other macrocytic without neurological involvement",
              "class": "C",
              "name": "hydroxycobalamine (IM)",
              "weight": "1mg",
              "frequency": "3 times a week for 2 weeks then 1mg (IM) every 3 months"
            },
            {
              "reason": "Pernicious Anaemia (B12 deficiency) with neurological symptoms and signs",
              "class": "C",
              "name": "hydroxycobalamine (IM)",
              "weight": "1mg",
              "frequency": "on alternate days until no further improvement then 1mg every 2-3 months"
            },
            {
              "reason": "Pernicious Anaemia (B12 deficiency) with neurological symptoms and signs",
              "class": "A",
              "name": "folic acid (PO)",
              "weight": "5mg",
              "frequency": "24hourly for at least 3 months"
            },
            {
              "reason": "Pernicious Anaemia (B12 deficiency) with neurological symptoms and signs",
              "class": "A",
              "name": "ferrous sulphate (PO)",
              "weight": "200mg",
              "frequency": "8hourly for at least 3 months"
            }
          ]
        }
      ],
      "notes": []
    },
    {
      "name": "Haemolytic Anaemia",
      "description": "Haemolytic anaemia results from an increase in the rate of red cell destruction in the intravascular or in the reticuloendothelial system in some pathological disorders",
      "clinical_presentation": "Pallor, jaundice, splenomegaly, Anaemia, Reticulocytosis, indirect hyperbilirubinemia, and haemoglobinuria",
      "investigations": [],
      "treatments": [
        {
          "Pharmacological Treatment": [
            {
              "class": "A",
              "name": "prednisolone (PO)",
              "weight": "1-1.5mg/kg/day",
              "frequency": "for 1-3 weeks until Hb > 10g/dl"
            },
            {
              "class": "S",
              "name": "cyclophosphamide (IV)",
              "weight": "50mg/kg/day",
              "frequency": "for 4 days"
            },
            {
              "class": "A",
              "name": "folic acid (PO)",
              "weight": "5mg",
              "frequency": "24hourly for 1-3 months"
            },
            {
              "class": "B",
              "name": "blood transfusion",
              "weight": "",
              "frequency": "",
              "total_time_for_usage": "",
              "conditions": "if anaemia is severe"
            },
            {
              "class": "S",
              "name": "High dose human immunoglobulin G (IV)",
              "weight": "400mg/kg/day",
              "frequency": "for 5 days"
            }
          ]
        },
        {
          "Surgical Management": [
            "Splenectomy may be considered in those who fail to respond to pharmacological treatment."
          ]
        }
      ],
      "notes": []
    },
    {
      "name": "Sickle Cell Disease (SCD)",
      "description": "The clinical manifestations of SCA are variable; Symptoms usually occur after 6 months of life. acute onset of unexplained illness, including acute pain, anaemia, acute neurological symptoms, loss of vision, respiratory infections, hepatosplenomegaly, jaundice, swollen limbs and sepsis.",
      "clinical_presentation": "",
      "investigations": [
        "Screening test: sickling test, isoelectric focusing (electrophoretic separation)",
        "Confirmatory Tests: Sickle Scan, haemoglobin electrophoresis, HPLC (High performance Liquid Chromatography)",
        "Other ancillary laboratory investigations useful in detection and monitoring of complications include: Haemoglobin, complete blood count, blood film morphology, Urea and electrolytes, serum bilirubin, Liver function tests"
      ],
      "treatments": [
        {
          "Non-Pharmacological Treatment": [
            {
              "Hydration and Electrolyte Balance": [
                "Maintain hydration and correct dehydration and electrolyte imbalance",
                "Patients with ACS should receive intravenous fluids at a rate sufficient to maintain adequate hydration (not overload), and oxygenation as needed."
              ]
            },
            {
              "Rest and Pain Management": [
                "Provide adequate rest and manage pain using WHO analgesic ladder (using paracetamol, NSAIDs and opioids if indicated)"
              ]
            }
          ]
        },
        {
          "Pharmacological Treatment": [
            {
              "Drugs to prevent infections": [
                {
                  "class": "A",
                  "name": "oral penicillin",
                  "weight": "125 mg",
                  "frequency": "12hourly up to 3 years",
                  "age_group": "children"
                },
                {
                  "class": "A",
                  "name": "oral penicillin",
                  "weight": "250 mg",
                  "frequency": "12hourly from 3 years until at least 15 years of age",
                  "age_group": "children"
                },
                {
                  "class": "B",
                  "name": "benzathine penicillin (IM)",
                  "weight": "600,000 units",
                  "frequency": "every 4 weeks for children < 27kg body weight",
                  "age_group": "children"
                },
                {
                  "class": "B",
                  "name": "benzathine penicillin (IM)",
                  "weight": "1.2 MU",
                  "frequency": "every 4 weeks for children ≥ 27 kg body weight and adults",
                  "age_group": "adults"
                },
                {
                  "class": "A",
                  "name": "folic acid",
                  "weight": "1-5 mg",
                  "frequency": "24hourly",
                  "age_group": "any"
                },
                {
                  "class": "S",
                  "name": "hydroxyurea",
                  "weight": "15-30mg/kg",
                  "frequency": "24hourly",
                  "age_group": "any"
                },
                {
                  "class": "A",
                  "name": "anti-malarial treatment (artemether lumefantrine (PO)",
                  "weight": "",
                  "frequency": "if required",
                  "age_group": "any"
                },
                {
                  "class": "B",
                  "name": "amoxicillin (PO)",
                  "weight": "",
                  "frequency": "if required",
                  "age_group": "any"
                }
              ]
            },
            {
              "Pain management during crises": [
                {
                  "class": "A",
                  "name": "morphine",
                  "weight": "",
                  "frequency": "",
                  "age_group": "any"
                },
                {
                  "class": "B",
                  "name": "pethidine",
                  "weight": "",
                  "frequency": "",
                  "age_group": "any"
                }
              ]
            }
          ]
        },
        {
          "Surgical Management": [
            {
              "note": "Surgical intervention may be necessary for certain complications of SCD, such as cholecystectomy for gallstones."
            }
          ]
        }
      ],
      "notes": []
    },  
      {
      "name": "Deep Vein Thrombosis (DVT)",
      "clinical_presentation": [
        "Leg pain, tenderness and swelling",
        "A palpable cord representing thrombosed vessels",
        "Discoloration, venous distention and prominence of superficial veins and cyanosis",
        "The clinical diagnosis of DVT is highly nonspecific"
      ],
      "investigations": [
        "D-dimer",
        "Doppler USS",
        "PT, INR, Aptt"
      ],
      "treatments": [
        {
          "Pharmacological Treatment": [
            {
              "class": "C",
              "name": "warfarin (PO)",
              "dose": "5mg 24hourly for 5 days, then adjust the dose according to INR levels for 3-6 months"
            },
            {
              "class": "S",
              "name": "Low Molecular weight heparin (SC)",
              "weight": "1mg/kg",
              "frequency": "24hourly for 5 days",
            },
            {
              "class": "S",
              "name": "Unfractionated heparin (IV)",
              'weight':"75units/kg",
              'frequency':"15–25 Units/kg/hr by IV infusion" ,
              'condition': ''
            },
            {
              "class": "S",
              "name": "Unfractionated heparin (IV)",
              'weight':"75units/kg",
              'frequency':"15–25 Units/kg/hr by IV infusion",
              "condition": "Adolescents or children"
            },
            {
              "class": "S",
              "name": "Unfractionated heparin (SC)",
              'weight':"250units/kg",
              'frequency':"12 hourly", 
              "condition": "Adolescents or children"
            },
            {
              "class": "S",
              "name": "rivaroxaban (PO)",
              "weight": "15mg",
              'frequency':"12 hourly for 21 days then 20mg 24hourly for the remaining duration of treatment",
            },
            {
              "class": "D",
              "name": "Low Molecular weight heparin (SC)",
              'weight':"1mg/kg",
              'frequency':"12hourly",
              "condition": "Pregnant women"
            }
          ]
        }
      ],
      "notes": [
        "Warfarin is teratogenic, therefore low molecular weight heparin is recommended during pregnancy."
      ]
    },
    {
      "name": "Pulmonary Embolism (PE)",
      "clinical_presentation": [
        "Transient dyspnea and tachypnea in the absence of other clinical features",
        "Pleuritic chest pain, cough, haemoptysis, pleural effusion, and pulmonary infiltrate",
        "Severe dyspnea and tachypnea and right-side heart failure",
        "Cardiovascular collapse with hypotension, syncope, and coma",
        "Several less common and nonspecific presentation including unexplained tachycardia or arrhythmia, resistant cardiac failure, wheezing, cough, fever, apprehension and confusion"
      ],
      "investigations": [
        "PT, INR, aPTT",
        "D-dimer",
        "CXR and CT angiography"
      ],
      "treatments": [
        {
          "Pharmacological Treatment": [
            {
              "class": "C",
              "name": "warfarin (PO)",
              'weight':"5mg",
              'frequency': '24hourly for 5 days',
              "dose": "5mg 24hourly for 5 days, then adjust the dose according to INR levels for 3-6 months"
            },
            {
              "class": "S",
              "name": "Low Molecular weight heparin (SC)",
              "dose": "1mg/kg 24hourly for 5 days",
              'weight':"1mg/kg",
              'frequency':"24hourly for 5 days"
            },
            {
              "class": "S",
              "name": "Unfractionated heparin (IV)",
              "dose": "75units/kg followed by continuous infusion of 18units/kg/hrs",
              'weight': '75units/kg',
              'frequency': '15–25 Units/kg/hr by IV infusion'
            },
            {
              "class": "S",
              "name": "Unfractionated heparin (IV)",
              "dose": "75units/kg then 15–25 Units/kg/hr by IV infusion",
              'weight':"75units/kg",
              'frequency':"15–25 Units/kg/hr by IV infusion",
              "condition": "Adolescents or children"
            },
            {
              "class": "S",
              "name": "Unfractionated heparin (SC)",
              "dose": "250units/kg 12hourly",
              'weight':"250units/kg",
              'frequency':"12 hourly",
              "condition": "Adolescents or children"
            },
            {
              "class": "S",
              "name": "rivaroxaban (PO)",
              "dose": "15mg 12hourly for 21 days, then 20mg 24hourly for the remaining duration of treatment",
              'weight':"15mg",
              'frequency':"12 hourly for 21 days, then 20mg 24hourly for the remaining duration of treatment"
            },
            {
              "class": "D",
              "name": "Low Molecular weight heparin (SC)",
              "dose": "1mg/kg 12hourly for the whole duration of treatment",
              "condition": "Pregnant women"
            }
          ]
        }
      ],
      "notes": [
        "Warfarin therapeutic INR ranges from 2 to 3 for VTE, and 2.5 -3.5 for patients with mechanical heart valves",
        "Warfarin therapy should be monitored by INR after 5 –7 days of treatment, then as needed throughout the duration of treatment",
        "If the cause of VTE is acquired thromboembolism, treatment lasts for 3-6 months, BUT if the cause is inherited thrombophilia, treatment is lifelong",
        "Warfarin interacts with many drugs therefore precaution should be taken when administered with other drugs",
        "If warfarin overdose/toxicity occurs, stop warfarin and give FFP 10-15mls/kg and vitamin K 5mg IV stat. Reinitiate warfarin after bleeding has stopped and INR is within therapeutic range, using the lower dosage",
        "For VTE prophylaxis in bedridden patients, give enoxaparin 40mg SC OR Rivaroxaban 10mg orally once a day until ambulation resume",
        "Unfractionated heparin should be monitored by aPTT before and during treatment"
      ]
    },
        {
      "name": "Rift Valley Fever",
      "description": "A viral disease that affects mainly animals and occasionally humans. The virus is a member of the Phlebovirus genus, one of the five genera in the family Bunyaviridae. The disease is frequently reported following heavy rainfall and floods.",
      "clinical_presentation": "The incubation period of RVF varies from 2 to 6 days. These symptoms usually last from 4 to 7 days. Most of the infected people recover on their own. However, a small proportion gets complications such as vomiting blood, nose bleeding and passing bloody stool. Rift Valley fever is difficult to distinguish from other viral haemorrhagic fevers as well as many other diseases that cause fever, including malaria, shigellosis, typhoid fever, and yellow fever.",
      "investigations": [
        "The virus detection in the blood then virus isolation in cell culture",
        "Molecular techniques (reverse transcriptase polymerase chain reaction or RT-PCR).",
        "Antibody testing using Enzyme-Linked ImmunoAssay (ELISA) confirms infection with RVFV",
        "IgM antibodies reflect a recent infection and IgG antibodies persist for several years (Detection of anti-RVF IgM suggests an ongoing transmission of RVFV in humans during inter-epidemic periods.).",
        "FBC o Low Hb [Hb<8gm/dL - Severe pallor o Low platelet < 100 x109 /Dl (Thrombocytopenia) – small skin and mucous membrane hemorrhages (Petechiae))",
        "Serum Creatinine"
      ],
      "notes": [
        "RVF is mainly transmitted from animals (sheep, cattle, goats, camels) to humans through close contact with infected animals (such as handling meat and body fluids and consumption of raw milk).",
        "During established RVF outbreaks in animals, humans can also get infected through bites of infected mosquitoes and other biting insects.",
        "Suspected case: Early Disease: Acute febrile illness (axillary temperature >37.5 ºC or oral temperature of >38.0ºC) of more than 48 hours’ duration that does not respond to antibiotic or antimalarial therapy, and is associated with: • Direct contact with sick or dead animal or its products AND / OR • Recent travel (during last week) to, or living in an area where, after heavy rains, livestock die or abort, and where RVF virus activity is suspected/confirmed AND / OR • Abrupt onset of any 1 or more of the following: exhaustion, backache, muscle pains, headache (often severe), discomfort when exposed to light, and nausea/vomiting AND / OR: • Nausea/vomiting, diarrhoea OR abdominal pain with 1 or more of the following: • Severe pallor (or Hb < 8 gm/dL) • Low platelets (thrombocytopenia) as evidence by presence of small skin and mucous membrane haemorrhages (petechiae) (or platelet count < 100x109 / d • Evidence of kidney failure (edema, reduced urine output) (or creatinine > 150 mol/L) AND / OR • Evidence of bleeding into skin, bleeding from puncture wounds, from mucous membranes or nosefrom gastrointestinal tract and unnatural bleeding from vagina AND / OR • Clinical jaundice (3-fold increase above normal of transaminases)",
        "Late stages of diseases or complications (2-3 weeks after onset) • Patients who have experienced, in the preceding month a flu-like illness, with clinical criteria, who additionally develop the following: o CNS manifestations which resemble meningo-encephalitis AND/OR: o Unexplained visual loss OR o Unexplained death following sudden onset of acute flu-like illness with haemorrhage, meningo-ecephalitis, or visual loss during the preceding month.",
        "Confirmed case: Any patient who, after clinical screening, is positive for anti-RVF IgM ELISA antibodies (typically appear from fourth to sixth day after onset of symptoms) or tests positive on reverse transcriptase polymerase chainreaction (RT-PCR).",
        "Transmission to human is mainly through direct or indirect contact with blood or organs of infected animals. The virus can be transmitted to human through; • Handling of animal tissue during slaughtering or butchering, assisting with animal births, conducting veterinary procedures. • Inoculation e.g via wound from infected knife or through contact with broken skin or through inhalation of aerosols produced during the slaughter of an infected animals. • Infected mosquito. Human become viraemic; capable of infecting mosquitoes shortly before onset of fever and for the first 3–5 days of illness. Once infected, mosquitoes remain so for life.",
        "Acute RVF can be diagnosed using several different methods 1. Serological tests such as ELISA may confirm the presence of specific IgM antibodies to the virus. The virus itself may be detected in blood during the early phase of illness or in post-mortem tissue using a variety of techniques including, antigen detection tests by ELISA, RT-PCR, virus propagation (in cell cultures), Immunohistochemistry in formalin-fixed tissues 2. ELISA IgG can be used for retrospective diagnostic."
      ],
      "treatments": [
        {
          "Non-Pharmacological Treatment": [
            {
                "Rift Valley Fever": [
                  "Protect people from contact with blood, body fluids, or tissues of infected animals. (Use PPEs like gloves, boots, long sleeves, and a face shield)",
                  "Protect people from unsafe animal products. All animal products (including meat, milk, and blood) should be thoroughly cooked before eating or drinking.",
                  "Protect people from mosquitoes and other bloodsucking insects. Use insect repellents and bed nets, and wear long sleeved shirts and long pants to cover exposed skin."
                ]
            }
          ]
        },
        {
          "Pharmacological Treatment": [
            {
              "age/Group": "All",
              "drugs": [
                {
                  "class": "A",
                  "name": "paracetamol",
                  "weight": "15mg/kg",
                  "frequency": "8 hourly",
                  "total_time_for_usage": "3 days"
                },
                {
                  "class": "B",
                  "name": "Oxygen",
                  "weight": "",
                  "frequency": "",
                  "total_time_for_usage": ""
                },
                {
                  "class": "B",
                  "name": "Manage hypoglycaemia",
                  "weight": "",
                  "frequency": "",
                  "total_time_for_usage": ""
                },
                {
                    
                  "class": "A",
                  "name": "compoundsodium lactate",
                  "weight": "",
                  "frequency": "",
                  "total_time_for_usage": ""
                },
                {
                  "class": "A",
                  "name": "NS",
                  "weight": "",
                  "frequency": "",
                  "total_time_for_usage": ""
                },
                {
                  "class": "B",
                  "name": "Oxygen therapy",
                  "weight": "",
                  "frequency": "",
                  "total_time_for_usage": ""
                },
                {
                  "class": "A",
                  "name": "compoundsodium lactate",
                  "weight": "",
                  "frequency": "",
                  "total_time_for_usage": ""
                },
                {
                  "class": "A",
                  "name": "NS",
                  "weight": "",
                  "frequency": "",
                  "total_time_for_usage": ""
                },
                {
                  "class": "A",
                  "name": "5% DNS",
                  "weight": "",
                  "frequency": "",
                  "total_time_for_usage": ""
                },
                {
                  "class": "A",
                  "name": "25% Dextrose Solution",
                  "weight": "",
                  "frequency": "",
                  "total_time_for_usage": ""
                },
                {
                  "class": "A",
                  "name": "Medication to support blood pressure",
                  "weight": "",
                  "frequency": "",
                  "total_time_for_usage": ""
                },
                {
                  "class": "A",
                  "name": "Medication to reduce vomiting and diarrhea",
                  "weight": "",
                  "frequency": "",
                  "total_time_for_usage": ""
                },
                {
                  "class": "A",
                  "name": "Medication to manage fever and pain",
                  "weight": "",
                  "frequency": "",
                  "total_time_for_usage": ""
                },
                {
                  "class": "A",
                  "name": "Treating other infections",
                  "weight": "",
                  "frequency": "",
                  "total_time_for_usage": ""
                },
                {
                  "class": "A",
                  "name": "Treating any complicating infection",
                  "weight": "",
                  "frequency": "",
                  "total_time_for_usage": ""
                },
                {
                  "class": "A",
                  "name": "Treating co-morbid condition",
                  "weight": "",
                  "frequency": "",
                  "total_time_for_usage": ""
                },
                {
                  "class": "A",
                  "name": "Psychological support",
                  "weight": "",
                  "frequency": "",
                  "total_time_for_usage": ""
                },
                {
                  "class": "C",
                  "name": "Mechanical ventilation",
                  "weight": "",
                  "frequency": "",
                  "total_time_for_usage": ""
                },
                {
                  "class": "C",
                  "name": "renal dialysis",
                  "weight": "",
                  "frequency": "",
                  "total_time_for_usage": ""
                },
                {
                  "class": "C",
                  "name": "anti-seizure therapy",
                  "weight": "",
                  "frequency": "",
                  "total_time_for_usage": ""
                }
              ]
            }
          ]
        }
      ]
    },{
      "name": "Yellow Fever",
      "description": "Yellow fever virus is an RNA that belongs to the genus Flavivirus and is related to West Nile, St. Louis encephalitis, and Japanese encephalitis viruses.",
      "clinical_presentation": "It is transmitted human-to-human via the domestic species of Aedes mosquitoes (Urban epidemics) or to humans from primate reservoir via a forest mosquito species (Sylvatic cycle). About 15% of infections progress to fever and jaundice. While only the minority of cases are severe, case fatality rate may be 25% to 50% among patients with syndrome of haemorrhage, jaundice, and renal disease. A small proportion of patients develop “toxic phase” with jaundice (yellowing of the skin and eyes, hence the name ‘yellow fever’), dark urine and abdominal pain with vomiting. Bleeding can occur from the mouth, nose, eyes or stomach and half of those die within 7 to 10 days.",
      "investigations": [
        "ELISA for the presence of yellow fever Specific IgM and IgG antibodies.",
        "Exclusion of Dengue, West Nile virus and other locally prevalent flavivirus will be necessary for the confirmation of yellow fever.",
        "PCR, YF specific seroneutralization, virus isolation or histopathology"
      ],
      "notes": [
        "Risk factor: Sporadic cases often linked to occupation or village location near woods or where monkeys are numerous, also non-vaccinated persons.",
        "Infection and disease can be prevented by vaccination.",
        "With a vaccine efficacy > 95% and duration of immunity is life time",
        "Suspected case: Any person with acute onset of fever, with jaundice appearing within 14 days of onset of the first symptoms.",
        "Probable case: A suspected case with one of the following; • Epidemiological link to a confirmed case or an outbreak • Positive post-mortem liver histopathology",
        "Confirmed case: A probable case with one of the following; • Detection of YF-specific* IgM • Detection of four-fold increase in YF IgM and/or IgG antibody titres between acute and convalescent serum samples • Detection of YFV-specific* neutralizing antibodies *YF-specific means that antibody tests (such as IgM or neutralizing antibody) for other prevalent flavivirus are negative. This testing should include at least IgM for Dengue and West Nile and may include other flavivirus depending on local epidemiology.",
        "OR One of the following • Detection of YF virus genome in blood or other organs by PCR Detection of yellow fever antigen in blood, liver or other organs by immunoassays Isolation of the yellow fever virus"
      ],
      "treatments": [
        {
          "Non-Pharmacological Treatment": [
            {
                "Yellow Fever": [
                  "Prevention and Control involve mosquito control and provision of Yellow Fever vaccine.",
                  "The yellow fever vaccine is safe, affordable and a single dose provides life-long protection against yellow fever disease."
                ]
              }
          ]
        },
        {
          "Pharmacological Treatment": [
            {
              "age/Group": "All",
              "drugs": [
                {
                  "class": "A",
                  "name": "Good and early supportive treatment for dehydration",
                  "weight": "",
                  "frequency": "",
                  "total_time_for_usage": ""
                },
                {
                  "class": "A",
                  "name": "Good and early supportive treatment for liver and kidney failure",
                  "weight": "",
                  "frequency": "",
                  "total_time_for_usage": ""
                },
                {
                  "class": "A",
                  "name": "Good and early supportive treatment for fever",
                  "weight": "",
                  "frequency": "",
                  "total_time_for_usage": ""
                },
                {
                  "class": "A",
                  "name": "Antibiotics",
                  "weight": "",
                  "frequency": "",
                  "total_time_for_usage": ""
                }
              ]
            }
          ]
        }
      ]
    },
     {
      "name": "Dengue Fever",
      "description": "Dengue virus is an arbovirus transmitted by aedes mosquitoes (both Ae. aegypti and Ae. albopiticus). Dengue fever is caused by four serologically distinct, but closely related Dengue viruses: dengue virus (DENV) 1, 2, 3, and 4 of the Flaviviridae family. Dengue fever is an emerging pandemic that has spread globally during the past 30 years as a result of changes in human ecology. Dengue haemorrhagic fever (DHF) is a potentially deadly complication that has become a leading cause of hospitalization and death among children in Asia and Africa. There is good evidence that sequential infection with the different serotypes of dengue virus increases the risk of more severe disease that can result in dengue shock syndrome (DSS) and death.",
      "clinical_presentation": "Infected humans are the main carriers and multipliers of the virus, serving a source of the virus for uninfected Aedes aegypti mosquitoes which maintain the urban dengue transmission cycle. The virus circulates in the blood of infected human for 2-7 days, at approximately the same time that they have a fever. A sylvatic transmission cycle has been documented in West Africa where DENV-2 has been found in monkeys. There is no evidence of person-to-person transmission.",
      "investigations": [
        "Reverse Transcriptase–Polymerase Chain Reaction (RT–PCR)",
        "Rapid Tests for Dengue NSI antigen",
        "Serological methods, such as Enzyme-Linked Immunosorbent Assays (ELISA) for IgM and IgG anti-dengue antibodiesFBP"
      ],
      "notes": [
        "DENV is frequently transported from one place to another by infected travelers; when susceptible vectors are present in these new areas, there is the potential for local transmission to be established.",
        "Dengue Fever Suspected case: Any person with acute febrile illness of 2-7 days duration with 2 or more of the following: headache, retro-orbital pain, myalgia, arthralgia, rash, haemorrhagic manifestations, leucopenia.",
        "Dengue Fever Confirmed case: A suspected case with laboratory confirmation (positive IgM antibody, four-fold or greater rise in IgG antibody titres, positive PCR or viral isolation).",
        "Dengue Haemorrhagic Fever: A probable or confirmed case of dengue with bleeding tendencies as evidenced by one or more of the following: positive tourniquet test; petechieae, ecchymoses or purpura; bleeding: mucosa, gastrointestinal tract, injection sites or other; haematemesis or melaena; and thrombocytopenia (100,000 cells or less per mm3) and evidence of plasma leakage due to increased vascular permeability, manifested by one or more of the following: 20% rise in average haematocrit for age and sex, 20% drop in haematocrit following volume replacement therapy compared to baseline, signs of plasma leakage (pleural effusion, ascites, hypo-proteinaemia).",
        "Dengue Shock Syndrome: All the above criteria, plus evidence of circulatory failure manifested by rapid and weak pulse, and narrow pulse pressure (≤ 20 mm Hg) or hypotension for age, cold, clammy skin and altered mental status."
      ],
      "treatments": [
        {
          "Non-Pharmacological Treatment": [
            {
                "Dengue Fever": [
                  "Prevent dengue by avoiding mosquito bites by Aedes. aegypti and Aedes. albopictus bite during the day and night (Using mosquito repellant, bed nets and removing reservoirs).",
                  "All four dengue viruses are spread primarily through the bite of an infected Aedes mosquito.",
                  "A dengue vaccine is available for use in some parts of"
                ]
            }
    ]
    }
    ]
},
    {
      "name": "Blood components",
      "description": "A single donation of blood can be separated into several blood components. Currently in Tanzania the following blood components are available for transfusion: packed red blood cells, Fresh Frozen Plasma, single unit platelet (plasma rich) and whole blood units."
    },
    {
      "name": "Whole blood",
      "description": "One unit contains 450mls of blood. It is poor in platelets and clotting factors and can be stored for 35days at 2-6°C.",
      "clinical_presentation": [
        "Exchange transfusion",
        "Open heart surgery",
        "In the absence of PRBCs in patients with acute blood loss and hypovolaemia"
      ],
      "notes": [
        "It can be stored for 35days at 2-6°C. One unit increases haemoglobin (Hb) level by approximately 1g/dl in adult, whereas in children, a dose of 10-15mls/kg will increase the Hb by about 3g/dl.",
        "Indications: acute blood loss, exchange transfusion, cardiac patients with Hb level <8g/dl, chronic symptomatic anaemia with Hb <5g/dl, preoperative patients with Hb level <8g/dl, pre-radiotherapy patients with Hb level <10g/dl, pre and post chemotherapy patients with Hb <9g/dl, and patients admitted to ICU with Hb <7g/dl."
      ],
      "treatments": {
        "Pharmacological Treatment": [
          {
            "age/Group": "Adults",
            "drugs": [
              {
                "class": "A",
                "name": "therapeutic",
                "weight": "50mls per 10kg 5-6 RDP units",
                "frequency": "8hourly",
                "total_time_for_usage": "3 months"
              }
            ]
          },
          {
            "age/Group": "infants",
            "drugs": [
              {
                "class": "A",
                "name": "therapeutic",
                "weight": "5mls/kg",
                "frequency": "8hourly",
                "total_time_for_usage": "3 months"
              }
            ]
          }
        ]
      }
    }
  ]
}

