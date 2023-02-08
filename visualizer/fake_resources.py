class Resources:
    MedicationProductDefinition = {
      "resourceType": "MedicinalProductDefinition",
      "id": "Panodil500mgoralsolutionsachet-SE-PLC-MPD",
      "meta": {
        "versionId": "1",
        "lastUpdated": "2023-01-27T16:49:39.612+00:00",
        "source": "#idgI4gwoENZUReIw",
        "profile": [
          "http://unicom-project.eu/fhir/StructureDefinition/PPLMedicinalProductDefinition"
        ]
      },
      "text": {
        "status": "generated",
        "div": "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p><b>Generated Narrative: MedicinalProductDefinition</b><a name=\"Panodil500mgoralsolutionsachet-SE-PLC-MPD\"> </a></p><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\">Resource MedicinalProductDefinition &quot;Panodil500mgoralsolutionsachet-SE-PLC-MPD&quot; </p><p style=\"margin-bottom: 0px\">Profile: <a href=\"StructureDefinition-PPLMedicinalProductDefinition.html\">PPL Medicinal Product profile</a></p></div><p><b>identifier</b>: id: SE-100004600-00012391</p><p><b>domain</b>: Human use <span style=\"background: LightGoldenRodYellow; margin: 4px; border: 1px solid khaki\"> (<a href=\"CodeSystem-domain-ema-cs.html\">Domain EMA</a>#100000000012)</span></p><p><b>status</b>: Current <span style=\"background: LightGoldenRodYellow; margin: 4px; border: 1px solid khaki\"> (<a href=\"CodeSystem-recordStatus-ema-cs.html\">Record Status EMA SPOR</a>#200000005004)</span></p><p><b>combinedPharmaceuticalDoseForm</b>: Powder for oral solution in sachet <span style=\"background: LightGoldenRodYellow; margin: 4px; border: 1px solid khaki\"> (<a href=\"CodeSystem-combined-term-ema-cs.html\">Combined Term EMA</a>#100000125752)</span></p><p><b>indication</b>: Panodil 500 mg pulver till oral lösning i dospåse används mot huvudvärk, tandvärk, feber vid förkylningssjukdomar, menstruationssmärtor, muskel- och ledvärk, som analgetikum vid reumatiska smärtor, hyperpyrexi. För vuxna och barn över 12 år.</p><p><b>legalStatusOfSupply</b>: Medicinal product not subject to medical prescription <span style=\"background: LightGoldenRodYellow; margin: 4px; border: 1px solid khaki\"> (<a href=\"CodeSystem-legal-status-for-the-supply-ema-cs.html\">Legal Status for the Supply EMA</a>#100000072076)</span></p><p><b>classification</b>: Paracetamol <span style=\"background: LightGoldenRodYellow; margin: 4px; border: 1px solid khaki\"> (<a href=\"CodeSystem-ATC-Human-EMA.html\">ATC Human EMA</a>#100000097305)</span>, Paracetamol <span style=\"background: LightGoldenRodYellow; margin: 4px; border: 1px solid khaki\"> (<a href=\"http://terminology.hl7.org/5.0.0/CodeSystem-v3-WC.html\">WHO ATC</a>#N02BE01)</span></p><blockquote><p><b>name</b></p><p><b>productName</b>: Panodil 500 mg pulver till oral lösning i dospåse</p><blockquote><p><b>namePart</b></p><p><b>part</b>: Panodil</p><p><b>type</b>: Invented name part <span style=\"background: LightGoldenRodYellow; margin: 4px; border: 1px solid khaki\"> (220000000000#220000000002)</span></p></blockquote><blockquote><p><b>namePart</b></p><p><b>part</b>: 500 mg</p><p><b>type</b>: Strength part <span style=\"background: LightGoldenRodYellow; margin: 4px; border: 1px solid khaki\"> (220000000000#220000000004)</span></p></blockquote><blockquote><p><b>namePart</b></p><p><b>part</b>: pulver till oral lösning i dospåse</p><p><b>type</b>: Pharmaceutical dose form part <span style=\"background: LightGoldenRodYellow; margin: 4px; border: 1px solid khaki\"> (220000000000#220000000005)</span></p></blockquote><h3>CountryLanguages</h3><table class=\"grid\"><tr><td>-</td><td><b>Country</b></td><td><b>Language</b></td></tr><tr><td>*</td><td>Kingdom of Sweden <span style=\"background: LightGoldenRodYellow; margin: 4px; border: 1px solid khaki\"> (<a href=\"CodeSystem-country-ema-cs.html\">Country EMA</a>#100000000535)</span></td><td>Swedish <span style=\"background: LightGoldenRodYellow; margin: 4px; border: 1px solid khaki\"> (<a href=\"CodeSystem-language-ema-cs.html\">Language EMA</a>#100000072288)</span></td></tr></table></blockquote></div>"
      },
      "identifier": [
        {
          "system": "http://ema.europa.eu/fhir/mpId",
          "value": "SE-100004600-00012391"
        }
      ],
      "domain": {
        "coding": [
          {
            "system": "https://spor.ema.europa.eu/v1/lists/100000000004",
            "code": "100000000012",
            "display": "Human use"
          }
        ]
      },
      "status": {
        "coding": [
          {
            "system": "https://spor.ema.europa.eu/v1/lists/200000005003",
            "code": "200000005004",
            "display": "Current"
          }
        ]
      },
      "combinedPharmaceuticalDoseForm": {
        "coding": [
          {
            "system": "https://spor.ema.europa.eu/v1/lists/200000000007",
            "code": "100000125752",
            "display": "Powder for oral solution in sachet"
          }
        ]
      },
      "indication": "Panodil 500 mg pulver till oral lösning i dospåse används mot huvudvärk, tandvärk, feber vid förkylningssjukdomar, menstruationssmärtor, muskel- och ledvärk, som analgetikum vid reumatiska smärtor, hyperpyrexi. För vuxna och barn över 12 år.",
      "legalStatusOfSupply": {
        "coding": [
          {
            "system": "https://spor.ema.europa.eu/v1/lists/100000072051",
            "code": "100000072076",
            "display": "Medicinal product not subject to medical prescription"
          }
        ]
      },
      "classification": [
        {
          "coding": [
            {
              "system": "https://spor.ema.europa.eu/v1/lists/100000093533",
              "code": "100000097305",
              "display": "Paracetamol"
            }
          ]
        },
        {
          "coding": [
            {
              "system": "http://www.whocc.no/atc",
              "code": "N02BE01",
              "display": "Paracetamol"
            }
          ]
        }
      ],
      "name": [
        {
          "productName": "Panodil 500 mg pulver till oral lösning i dospåse",
          "namePart": [
            {
              "part": "Panodil",
              "type": {
                "coding": [
                  {
                    "system": "https://spor.ema.europa.eu/v1/lists/220000000000",
                    "code": "220000000002",
                    "display": "Invented name part"
                  }
                ]
              }
            },
            {
              "part": "500 mg",
              "type": {
                "coding": [
                  {
                    "system": "https://spor.ema.europa.eu/v1/lists/220000000000",
                    "code": "220000000004",
                    "display": "Strength part"
                  }
                ]
              }
            },
            {
              "part": "pulver till oral lösning i dospåse",
              "type": {
                "coding": [
                  {
                    "system": "https://spor.ema.europa.eu/v1/lists/220000000000",
                    "code": "220000000005",
                    "display": "Pharmaceutical dose form part"
                  }
                ]
              }
            }
          ],
          "countryLanguage": [
            {
              "country": {
                "coding": [
                  {
                    "system": "https://spor.ema.europa.eu/v1/lists/100000000002",
                    "code": "100000000535",
                    "display": "Kingdom of Sweden"
                  }
                ]
              },
              "language": {
                "coding": [
                  {
                    "system": "https://spor.ema.europa.eu/v1/lists/100000072057",
                    "code": "100000072288",
                    "display": "Swedish"
                  }
                ]
              }
            }
          ]
        }
      ]
    }

    AdministrableProductDefinitionBundle = {
      "resourceType": "Bundle",
      "id": "08b09b2f-b1c3-4894-b53c-55598c92cac4",
      "meta": {
        "lastUpdated": "2023-01-29T14:14:57.747+00:00"
      },
      "type": "searchset",
      "link": [
        {
          "relation": "self",
          "url": "https://jpa.unicom.datawizard.it/fhir/AdministrableProductDefinition"
        },
        {
          "relation": "next",
          "url": "https://jpa.unicom.datawizard.it/fhir?_getpages=08b09b2f-b1c3-4894-b53c-55598c92cac4&_getpagesoffset=20&_count=20&_pretty=true&_bundletype=searchset"
        }
      ],
      "entry": [
        {
          "fullUrl": "https://jpa.unicom.datawizard.it/fhir/AdministrableProductDefinition/AMLkrka-5mg-Tablet-SE-IS-AdministrableProductDefinition",
          "resource": {
            "resourceType": "AdministrableProductDefinition",
            "id": "AMLkrka-5mg-Tablet-SE-IS-AdministrableProductDefinition",
            "meta": {
              "versionId": "1",
              "lastUpdated": "2023-01-27T16:49:47.541+00:00",
              "source": "#lJeAH3hni0Rd12sc",
              "profile": [
                "http://unicom-project.eu/fhir/StructureDefinition/PPLAdministrableProductDefinition"
              ]
            },
            "text": {
              "status": "generated",
              "div": "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p><b>Generated Narrative: AdministrableProductDefinition</b><a name=\"AMLkrka-5mg-Tablet-SE-IS-AdministrableProductDefinition\"> </a></p><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\">Resource AdministrableProductDefinition &quot;AMLkrka-5mg-Tablet-SE-IS-AdministrableProductDefinition&quot; </p><p style=\"margin-bottom: 0px\">Profile: <a href=\"StructureDefinition-PPLAdministrableProductDefinition.html\">PPL Administrable Product profile</a></p></div><p><b>status</b>: active</p><p><b>formOf</b>: <a href=\"#MedicinalProductDefinition_AMLkrka-5mg-Tablet-SE-IS-MedicinalProductDefinition\">See above (MedicinalProductDefinition/AMLkrka-5mg-Tablet-SE-IS-MedicinalProductDefinition)</a></p><p><b>administrableDoseForm</b>: Tablet <span style=\"background: LightGoldenRodYellow; margin: 4px; border: 1px solid khaki\"> (<a href=\"CodeSystem-pharmaceutical-dose-form-ema-cs.html\">Pharmaceutical Dose Form EMA</a>#100000073664)</span></p><p><b>unitOfPresentation</b>: Tablet <span style=\"background: LightGoldenRodYellow; margin: 4px; border: 1px solid khaki\"> (<a href=\"CodeSystem-unit-of-presentation-ema-cs.html\">Unit of Presentation EMA</a>#200000002152)</span></p><p><b>producedFrom</b>: <a href=\"#ManufacturedItemDefinition_AMLkrka-5mg-Tablet-SE-IS-ManufacturedItemDefinition\">See above (ManufacturedItemDefinition/AMLkrka-5mg-Tablet-SE-IS-ManufacturedItemDefinition)</a></p><h3>RouteOfAdministrations</h3><table class=\"grid\"><tr><td>-</td><td><b>Code</b></td></tr><tr><td>*</td><td>Oral use <span style=\"background: LightGoldenRodYellow; margin: 4px; border: 1px solid khaki\"> (<a href=\"CodeSystem-routes-and-methods-of-administration-ema-cs.html\">Routes and Methods of Administration EMA</a>#100000073619)</span></td></tr></table></div>"
            },
            "status": "active",
            "formOf": [
              {
                "reference": "MedicinalProductDefinition/AMLkrka-5mg-Tablet-SE-IS-MedicinalProductDefinition"
              }
            ],
            "administrableDoseForm": {
              "coding": [
                {
                  "system": "https://spor.ema.europa.eu/v1/lists/200000000004",
                  "code": "100000073664",
                  "display": "Tablet"
                }
              ]
            },
            "unitOfPresentation": {
              "coding": [
                {
                  "system": "https://spor.ema.europa.eu/v1/lists/200000000014",
                  "code": "200000002152",
                  "display": "Tablet"
                }
              ]
            },
            "producedFrom": [
              {
                "reference": "ManufacturedItemDefinition/AMLkrka-5mg-Tablet-SE-IS-ManufacturedItemDefinition"
              }
            ],
            "routeOfAdministration": [
              {
                "code": {
                  "coding": [
                    {
                      "system": "https://spor.ema.europa.eu/v1/lists/100000073345",
                      "code": "100000073619",
                      "display": "Oral use"
                    }
                  ]
                }
              }
            ]
          },
          "search": {
            "mode": "match"
          }
        },
        {
          "fullUrl": "https://jpa.unicom.datawizard.it/fhir/AdministrableProductDefinition/Betaklav-500mg-125mg-EE-APD",
          "resource": {
            "resourceType": "AdministrableProductDefinition",
            "id": "Betaklav-500mg-125mg-EE-APD",
            "meta": {
              "versionId": "1",
              "lastUpdated": "2023-01-27T16:49:49.521+00:00",
              "source": "#cMMrML80UlQtJVfm",
              "profile": [
                "http://unicom-project.eu/fhir/StructureDefinition/PPLAdministrableProductDefinition"
              ]
            },
            "text": {
              "status": "generated",
              "div": "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p><b>Generated Narrative: AdministrableProductDefinition</b><a name=\"Betaklav-500mg-125mg-EE-APD\"> </a></p><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\">Resource AdministrableProductDefinition &quot;Betaklav-500mg-125mg-EE-APD&quot; </p><p style=\"margin-bottom: 0px\">Profile: <a href=\"StructureDefinition-PPLAdministrableProductDefinition.html\">PPL Administrable Product profile</a></p></div><p><b>status</b>: active</p><p><b>formOf</b>: <a href=\"#MedicinalProductDefinition_Betaklav-500mg-125mg-EE-MPD\">See above (MedicinalProductDefinition/Betaklav-500mg-125mg-EE-MPD)</a></p><p><b>administrableDoseForm</b>: Film-coated tablet <span style=\"background: LightGoldenRodYellow; margin: 4px; border: 1px solid khaki\"> (<a href=\"CodeSystem-pharmaceutical-dose-form-ema-cs.html\">Pharmaceutical Dose Form EMA</a>#100000073665)</span></p><p><b>unitOfPresentation</b>: Tablet <span style=\"background: LightGoldenRodYellow; margin: 4px; border: 1px solid khaki\"> (<a href=\"CodeSystem-unit-of-presentation-ema-cs.html\">Unit of Presentation EMA</a>#200000002152)</span></p><p><b>producedFrom</b>: <a href=\"#ManufacturedItemDefinition_Betaklav-500mg-125mg-EE-MID\">See above (ManufacturedItemDefinition/Betaklav-500mg-125mg-EE-MID)</a></p><h3>RouteOfAdministrations</h3><table class=\"grid\"><tr><td>-</td><td><b>Code</b></td></tr><tr><td>*</td><td>Oral use <span style=\"background: LightGoldenRodYellow; margin: 4px; border: 1px solid khaki\"> (<a href=\"CodeSystem-routes-and-methods-of-administration-ema-cs.html\">Routes and Methods of Administration EMA</a>#100000073619)</span></td></tr></table></div>"
            },
            "status": "active",
            "formOf": [
              {
                "reference": "MedicinalProductDefinition/Betaklav-500mg-125mg-EE-MPD"
              }
            ],
            "administrableDoseForm": {
              "coding": [
                {
                  "system": "https://spor.ema.europa.eu/v1/lists/200000000004",
                  "code": "100000073665",
                  "display": "Film-coated tablet"
                }
              ]
            },
            "unitOfPresentation": {
              "coding": [
                {
                  "system": "https://spor.ema.europa.eu/v1/lists/200000000014",
                  "code": "200000002152",
                  "display": "Tablet"
                }
              ]
            },
            "producedFrom": [
              {
                "reference": "ManufacturedItemDefinition/Betaklav-500mg-125mg-EE-MID"
              }
            ],
            "routeOfAdministration": [
              {
                "code": {
                  "coding": [
                    {
                      "system": "https://spor.ema.europa.eu/v1/lists/100000073345",
                      "code": "100000073619",
                      "display": "Oral use"
                    }
                  ]
                }
              }
            ]
          },
          "search": {
            "mode": "match"
          }
        },
        {
          "fullUrl": "https://jpa.unicom.datawizard.it/fhir/AdministrableProductDefinition/CopaliaHCT-EE-APD",
          "resource": {
            "resourceType": "AdministrableProductDefinition",
            "id": "CopaliaHCT-EE-APD",
            "meta": {
              "versionId": "1",
              "lastUpdated": "2023-01-27T16:49:49.914+00:00",
              "source": "#9AvP1FMnyLeqdsUs",
              "profile": [
                "http://unicom-project.eu/fhir/StructureDefinition/PPLAdministrableProductDefinition"
              ]
            },
            "text": {
              "status": "generated",
              "div": "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p><b>Generated Narrative: AdministrableProductDefinition</b><a name=\"CopaliaHCT-EE-APD\"> </a></p><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\">Resource AdministrableProductDefinition &quot;CopaliaHCT-EE-APD&quot; </p><p style=\"margin-bottom: 0px\">Profile: <a href=\"StructureDefinition-PPLAdministrableProductDefinition.html\">PPL Administrable Product profile</a></p></div><p><b>status</b>: active</p><p><b>formOf</b>: <a href=\"#MedicinalProductDefinition_CopaliaHCT-EE-MPD\">See above (MedicinalProductDefinition/CopaliaHCT-EE-MPD)</a></p><p><b>administrableDoseForm</b>: Film-coated tablet <span style=\"background: LightGoldenRodYellow; margin: 4px; border: 1px solid khaki\"> (<a href=\"CodeSystem-pharmaceutical-dose-form-ema-cs.html\">Pharmaceutical Dose Form EMA</a>#100000073665)</span></p><p><b>unitOfPresentation</b>: Tablet <span style=\"background: LightGoldenRodYellow; margin: 4px; border: 1px solid khaki\"> (<a href=\"CodeSystem-unit-of-presentation-ema-cs.html\">Unit of Presentation EMA</a>#200000002152)</span></p><h3>RouteOfAdministrations</h3><table class=\"grid\"><tr><td>-</td><td><b>Code</b></td></tr><tr><td>*</td><td>Oral use <span style=\"background: LightGoldenRodYellow; margin: 4px; border: 1px solid khaki\"> (<a href=\"CodeSystem-routes-and-methods-of-administration-ema-cs.html\">Routes and Methods of Administration EMA</a>#100000073619)</span></td></tr></table></div>"
            },
            "status": "active",
            "formOf": [
              {
                "reference": "MedicinalProductDefinition/CopaliaHCT-EE-MPD"
              }
            ],
            "administrableDoseForm": {
              "coding": [
                {
                  "system": "https://spor.ema.europa.eu/v1/lists/200000000004",
                  "code": "100000073665",
                  "display": "Film-coated tablet"
                }
              ]
            },
            "unitOfPresentation": {
              "coding": [
                {
                  "system": "https://spor.ema.europa.eu/v1/lists/200000000014",
                  "code": "200000002152",
                  "display": "Tablet"
                }
              ]
            },
            "routeOfAdministration": [
              {
                "code": {
                  "coding": [
                    {
                      "system": "https://spor.ema.europa.eu/v1/lists/100000073345",
                      "code": "100000073619",
                      "display": "Oral use"
                    }
                  ]
                }
              }
            ]
          },
          "search": {
            "mode": "match"
          }
        },
        {
          "fullUrl": "https://jpa.unicom.datawizard.it/fhir/AdministrableProductDefinition/AMLaurobindo-10mg-Tablet-SE-IS-AdministrableProductDefinition",
          "resource": {
            "resourceType": "AdministrableProductDefinition",
            "id": "AMLaurobindo-10mg-Tablet-SE-IS-AdministrableProductDefinition",
            "meta": {
              "versionId": "1",
              "lastUpdated": "2023-01-27T16:49:50.231+00:00",
              "source": "#zRTPQUmtuPfPnytl",
              "profile": [
                "http://unicom-project.eu/fhir/StructureDefinition/PPLAdministrableProductDefinition"
              ]
            },
            "text": {
              "status": "generated",
              "div": "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p><b>Generated Narrative: AdministrableProductDefinition</b><a name=\"AMLaurobindo-10mg-Tablet-SE-IS-AdministrableProductDefinition\"> </a></p><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\">Resource AdministrableProductDefinition &quot;AMLaurobindo-10mg-Tablet-SE-IS-AdministrableProductDefinition&quot; </p><p style=\"margin-bottom: 0px\">Profile: <a href=\"StructureDefinition-PPLAdministrableProductDefinition.html\">PPL Administrable Product profile</a></p></div><p><b>status</b>: active</p><p><b>formOf</b>: <a href=\"#MedicinalProductDefinition_AMLaurobindo-10mg-Tablet-SE-IS-MedicinalProductDefinition\">See above (MedicinalProductDefinition/AMLaurobindo-10mg-Tablet-SE-IS-MedicinalProductDefinition)</a></p><p><b>administrableDoseForm</b>: Tablet <span style=\"background: LightGoldenRodYellow; margin: 4px; border: 1px solid khaki\"> (<a href=\"CodeSystem-pharmaceutical-dose-form-ema-cs.html\">Pharmaceutical Dose Form EMA</a>#100000073664)</span></p><p><b>unitOfPresentation</b>: Tablet <span style=\"background: LightGoldenRodYellow; margin: 4px; border: 1px solid khaki\"> (<a href=\"CodeSystem-unit-of-presentation-ema-cs.html\">Unit of Presentation EMA</a>#200000002152)</span></p><p><b>producedFrom</b>: <a href=\"#ManufacturedItemDefinition_AMLaurobindo-10mg-Tablet-SE-IS-ManufacturedItemDefinition\">See above (ManufacturedItemDefinition/AMLaurobindo-10mg-Tablet-SE-IS-ManufacturedItemDefinition)</a></p><h3>RouteOfAdministrations</h3><table class=\"grid\"><tr><td>-</td><td><b>Code</b></td></tr><tr><td>*</td><td>Oral use <span style=\"background: LightGoldenRodYellow; margin: 4px; border: 1px solid khaki\"> (<a href=\"CodeSystem-routes-and-methods-of-administration-ema-cs.html\">Routes and Methods of Administration EMA</a>#100000073619)</span></td></tr></table></div>"
            },
            "status": "active",
            "formOf": [
              {
                "reference": "MedicinalProductDefinition/AMLaurobindo-10mg-Tablet-SE-IS-MedicinalProductDefinition"
              }
            ],
            "administrableDoseForm": {
              "coding": [
                {
                  "system": "https://spor.ema.europa.eu/v1/lists/200000000004",
                  "code": "100000073664",
                  "display": "Tablet"
                }
              ]
            },
            "unitOfPresentation": {
              "coding": [
                {
                  "system": "https://spor.ema.europa.eu/v1/lists/200000000014",
                  "code": "200000002152",
                  "display": "Tablet"
                }
              ]
            },
            "producedFrom": [
              {
                "reference": "ManufacturedItemDefinition/AMLaurobindo-10mg-Tablet-SE-IS-ManufacturedItemDefinition"
              }
            ],
            "routeOfAdministration": [
              {
                "code": {
                  "coding": [
                    {
                      "system": "https://spor.ema.europa.eu/v1/lists/100000073345",
                      "code": "100000073619",
                      "display": "Oral use"
                    }
                  ]
                }
              }
            ]
          },
          "search": {
            "mode": "match"
          }
        },
        {
          "fullUrl": "https://jpa.unicom.datawizard.it/fhir/AdministrableProductDefinition/AMLjubilant-5mg-Tablet-SE-IS-AdministrableProductDefinition",
          "resource": {
            "resourceType": "AdministrableProductDefinition",
            "id": "AMLjubilant-5mg-Tablet-SE-IS-AdministrableProductDefinition",
            "meta": {
              "versionId": "1",
              "lastUpdated": "2023-01-27T16:49:50.586+00:00",
              "source": "#dZ174YRXApdRfalQ",
              "profile": [
                "http://unicom-project.eu/fhir/StructureDefinition/PPLAdministrableProductDefinition"
              ]
            },
            "text": {
              "status": "generated",
              "div": "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p><b>Generated Narrative: AdministrableProductDefinition</b><a name=\"AMLjubilant-5mg-Tablet-SE-IS-AdministrableProductDefinition\"> </a></p><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\">Resource AdministrableProductDefinition &quot;AMLjubilant-5mg-Tablet-SE-IS-AdministrableProductDefinition&quot; </p><p style=\"margin-bottom: 0px\">Profile: <a href=\"StructureDefinition-PPLAdministrableProductDefinition.html\">PPL Administrable Product profile</a></p></div><p><b>status</b>: active</p><p><b>formOf</b>: <a href=\"#MedicinalProductDefinition_AMLjubilant-5mg-Tablet-SE-IS-MedicinalProductDefinition\">See above (MedicinalProductDefinition/AMLjubilant-5mg-Tablet-SE-IS-MedicinalProductDefinition)</a></p><p><b>administrableDoseForm</b>: Tablet <span style=\"background: LightGoldenRodYellow; margin: 4px; border: 1px solid khaki\"> (<a href=\"CodeSystem-pharmaceutical-dose-form-ema-cs.html\">Pharmaceutical Dose Form EMA</a>#100000073664)</span></p><p><b>unitOfPresentation</b>: Tablet <span style=\"background: LightGoldenRodYellow; margin: 4px; border: 1px solid khaki\"> (<a href=\"CodeSystem-unit-of-presentation-ema-cs.html\">Unit of Presentation EMA</a>#200000002152)</span></p><p><b>producedFrom</b>: <a href=\"#ManufacturedItemDefinition_AMLjubilant-5mg-Tablet-SE-IS-ManufacturedItemDefinition\">See above (ManufacturedItemDefinition/AMLjubilant-5mg-Tablet-SE-IS-ManufacturedItemDefinition)</a></p><h3>RouteOfAdministrations</h3><table class=\"grid\"><tr><td>-</td><td><b>Code</b></td></tr><tr><td>*</td><td>Oral use <span style=\"background: LightGoldenRodYellow; margin: 4px; border: 1px solid khaki\"> (<a href=\"CodeSystem-routes-and-methods-of-administration-ema-cs.html\">Routes and Methods of Administration EMA</a>#100000073619)</span></td></tr></table></div>"
            },
            "status": "active",
            "formOf": [
              {
                "reference": "MedicinalProductDefinition/AMLjubilant-5mg-Tablet-SE-IS-MedicinalProductDefinition"
              }
            ],
            "administrableDoseForm": {
              "coding": [
                {
                  "system": "https://spor.ema.europa.eu/v1/lists/200000000004",
                  "code": "100000073664",
                  "display": "Tablet"
                }
              ]
            },
            "unitOfPresentation": {
              "coding": [
                {
                  "system": "https://spor.ema.europa.eu/v1/lists/200000000014",
                  "code": "200000002152",
                  "display": "Tablet"
                }
              ]
            },
            "producedFrom": [
              {
                "reference": "ManufacturedItemDefinition/AMLjubilant-5mg-Tablet-SE-IS-ManufacturedItemDefinition"
              }
            ],
            "routeOfAdministration": [
              {
                "code": {
                  "coding": [
                    {
                      "system": "https://spor.ema.europa.eu/v1/lists/100000073345",
                      "code": "100000073619",
                      "display": "Oral use"
                    }
                  ]
                }
              }
            ]
          },
          "search": {
            "mode": "match"
          }
        },
        {
          "fullUrl": "https://jpa.unicom.datawizard.it/fhir/AdministrableProductDefinition/Agen-5mg-Tablet-EE-APD",
          "resource": {
            "resourceType": "AdministrableProductDefinition",
            "id": "Agen-5mg-Tablet-EE-APD",
            "meta": {
              "versionId": "1",
              "lastUpdated": "2023-01-27T16:49:51.022+00:00",
              "source": "#ehTM2OVKxzfT8GEG",
              "profile": [
                "http://unicom-project.eu/fhir/StructureDefinition/PPLAdministrableProductDefinition"
              ]
            },
            "text": {
              "status": "generated",
              "div": "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p><b>Generated Narrative: AdministrableProductDefinition</b><a name=\"Agen-5mg-Tablet-EE-APD\"> </a></p><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\">Resource AdministrableProductDefinition &quot;Agen-5mg-Tablet-EE-APD&quot; </p><p style=\"margin-bottom: 0px\">Profile: <a href=\"StructureDefinition-PPLAdministrableProductDefinition.html\">PPL Administrable Product profile</a></p></div><p><b>status</b>: active</p><p><b>formOf</b>: <a href=\"#MedicinalProductDefinition_Agen-5mg-Tablet-EE-MPD\">See above (MedicinalProductDefinition/Agen-5mg-Tablet-EE-MPD)</a></p><p><b>administrableDoseForm</b>: Tablet <span style=\"background: LightGoldenRodYellow; margin: 4px; border: 1px solid khaki\"> (<a href=\"CodeSystem-pharmaceutical-dose-form-ema-cs.html\">Pharmaceutical Dose Form EMA</a>#100000073664)</span></p><p><b>unitOfPresentation</b>: Tablet <span style=\"background: LightGoldenRodYellow; margin: 4px; border: 1px solid khaki\"> (<a href=\"CodeSystem-unit-of-presentation-ema-cs.html\">Unit of Presentation EMA</a>#200000002152)</span></p><p><b>producedFrom</b>: <a href=\"#ManufacturedItemDefinition_Agen-5mg-Tablet-EE-MID\">See above (ManufacturedItemDefinition/Agen-5mg-Tablet-EE-MID)</a></p><h3>RouteOfAdministrations</h3><table class=\"grid\"><tr><td>-</td><td><b>Code</b></td></tr><tr><td>*</td><td>Oral use <span style=\"background: LightGoldenRodYellow; margin: 4px; border: 1px solid khaki\"> (<a href=\"CodeSystem-routes-and-methods-of-administration-ema-cs.html\">Routes and Methods of Administration EMA</a>#100000073619)</span></td></tr></table></div>"
            },
            "status": "active",
            "formOf": [
              {
                "reference": "MedicinalProductDefinition/Agen-5mg-Tablet-EE-MPD"
              }
            ],
            "administrableDoseForm": {
              "coding": [
                {
                  "system": "https://spor.ema.europa.eu/v1/lists/200000000004",
                  "code": "100000073664",
                  "display": "Tablet"
                }
              ]
            },
            "unitOfPresentation": {
              "coding": [
                {
                  "system": "https://spor.ema.europa.eu/v1/lists/200000000014",
                  "code": "200000002152",
                  "display": "Tablet"
                }
              ]
            },
            "producedFrom": [
              {
                "reference": "ManufacturedItemDefinition/Agen-5mg-Tablet-EE-MID"
              }
            ],
            "routeOfAdministration": [
              {
                "code": {
                  "coding": [
                    {
                      "system": "https://spor.ema.europa.eu/v1/lists/100000073345",
                      "code": "100000073619",
                      "display": "Oral use"
                    }
                  ]
                }
              }
            ]
          },
          "search": {
            "mode": "match"
          }
        },
        {
          "fullUrl": "https://jpa.unicom.datawizard.it/fhir/AdministrableProductDefinition/AMLjubilant-10mg-Tablet-SE-IS-AdministrableProductDefinition",
          "resource": {
            "resourceType": "AdministrableProductDefinition",
            "id": "AMLjubilant-10mg-Tablet-SE-IS-AdministrableProductDefinition",
            "meta": {
              "versionId": "1",
              "lastUpdated": "2023-01-27T16:49:51.387+00:00",
              "source": "#YJ4JFge6IDDo6zXY",
              "profile": [
                "http://unicom-project.eu/fhir/StructureDefinition/PPLAdministrableProductDefinition"
              ]
            },
            "text": {
              "status": "generated",
              "div": "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p><b>Generated Narrative: AdministrableProductDefinition</b><a name=\"AMLjubilant-10mg-Tablet-SE-IS-AdministrableProductDefinition\"> </a></p><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\">Resource AdministrableProductDefinition &quot;AMLjubilant-10mg-Tablet-SE-IS-AdministrableProductDefinition&quot; </p><p style=\"margin-bottom: 0px\">Profile: <a href=\"StructureDefinition-PPLAdministrableProductDefinition.html\">PPL Administrable Product profile</a></p></div><p><b>status</b>: active</p><p><b>formOf</b>: <a href=\"#MedicinalProductDefinition_AMLjubilant-10mg-Tablet-SE-IS-MedicinalProductDefinition\">See above (MedicinalProductDefinition/AMLjubilant-10mg-Tablet-SE-IS-MedicinalProductDefinition)</a></p><p><b>administrableDoseForm</b>: Tablet <span style=\"background: LightGoldenRodYellow; margin: 4px; border: 1px solid khaki\"> (<a href=\"CodeSystem-pharmaceutical-dose-form-ema-cs.html\">Pharmaceutical Dose Form EMA</a>#100000073664)</span></p><p><b>unitOfPresentation</b>: Tablet <span style=\"background: LightGoldenRodYellow; margin: 4px; border: 1px solid khaki\"> (<a href=\"CodeSystem-unit-of-presentation-ema-cs.html\">Unit of Presentation EMA</a>#200000002152)</span></p><p><b>producedFrom</b>: <a href=\"#ManufacturedItemDefinition_AMLjubilant-10mg-Tablet-SE-IS-ManufacturedItemDefinition\">See above (ManufacturedItemDefinition/AMLjubilant-10mg-Tablet-SE-IS-ManufacturedItemDefinition)</a></p><h3>RouteOfAdministrations</h3><table class=\"grid\"><tr><td>-</td><td><b>Code</b></td></tr><tr><td>*</td><td>Oral use <span style=\"background: LightGoldenRodYellow; margin: 4px; border: 1px solid khaki\"> (<a href=\"CodeSystem-routes-and-methods-of-administration-ema-cs.html\">Routes and Methods of Administration EMA</a>#100000073619)</span></td></tr></table></div>"
            },
            "status": "active",
            "formOf": [
              {
                "reference": "MedicinalProductDefinition/AMLjubilant-10mg-Tablet-SE-IS-MedicinalProductDefinition"
              }
            ],
            "administrableDoseForm": {
              "coding": [
                {
                  "system": "https://spor.ema.europa.eu/v1/lists/200000000004",
                  "code": "100000073664",
                  "display": "Tablet"
                }
              ]
            },
            "unitOfPresentation": {
              "coding": [
                {
                  "system": "https://spor.ema.europa.eu/v1/lists/200000000014",
                  "code": "200000002152",
                  "display": "Tablet"
                }
              ]
            },
            "producedFrom": [
              {
                "reference": "ManufacturedItemDefinition/AMLjubilant-10mg-Tablet-SE-IS-ManufacturedItemDefinition"
              }
            ],
            "routeOfAdministration": [
              {
                "code": {
                  "coding": [
                    {
                      "system": "https://spor.ema.europa.eu/v1/lists/100000073345",
                      "code": "100000073619",
                      "display": "Oral use"
                    }
                  ]
                }
              }
            ]
          },
          "search": {
            "mode": "match"
          }
        },
        {
          "fullUrl": "https://jpa.unicom.datawizard.it/fhir/AdministrableProductDefinition/Norvasc-5mg-Tablet-SE-IS-AdministrableProductDefinition",
          "resource": {
            "resourceType": "AdministrableProductDefinition",
            "id": "Norvasc-5mg-Tablet-SE-IS-AdministrableProductDefinition",
            "meta": {
              "versionId": "1",
              "lastUpdated": "2023-01-27T16:49:51.745+00:00",
              "source": "#S4h26OteBQNvLXCE",
              "profile": [
                "http://unicom-project.eu/fhir/StructureDefinition/PPLAdministrableProductDefinition"
              ]
            },
            "text": {
              "status": "generated",
              "div": "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p><b>Generated Narrative: AdministrableProductDefinition</b><a name=\"Norvasc-5mg-Tablet-SE-IS-AdministrableProductDefinition\"> </a></p><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\">Resource AdministrableProductDefinition &quot;Norvasc-5mg-Tablet-SE-IS-AdministrableProductDefinition&quot; </p><p style=\"margin-bottom: 0px\">Profile: <a href=\"StructureDefinition-PPLAdministrableProductDefinition.html\">PPL Administrable Product profile</a></p></div><p><b>status</b>: active</p><p><b>formOf</b>: <a href=\"#MedicinalProductDefinition_Norvasc-5mg-Tablet-SE-IS-MedicinalProductDefinition\">See above (MedicinalProductDefinition/Norvasc-5mg-Tablet-SE-IS-MedicinalProductDefinition)</a></p><p><b>administrableDoseForm</b>: Tablet <span style=\"background: LightGoldenRodYellow; margin: 4px; border: 1px solid khaki\"> (<a href=\"CodeSystem-pharmaceutical-dose-form-ema-cs.html\">Pharmaceutical Dose Form EMA</a>#100000073664)</span></p><p><b>unitOfPresentation</b>: Tablet <span style=\"background: LightGoldenRodYellow; margin: 4px; border: 1px solid khaki\"> (<a href=\"CodeSystem-unit-of-presentation-ema-cs.html\">Unit of Presentation EMA</a>#200000002152)</span></p><p><b>producedFrom</b>: <a href=\"#ManufacturedItemDefinition_Norvasc-5mg-Tablet-SE-IS-ManufacturedItemDefinition\">See above (ManufacturedItemDefinition/Norvasc-5mg-Tablet-SE-IS-ManufacturedItemDefinition)</a></p><h3>RouteOfAdministrations</h3><table class=\"grid\"><tr><td>-</td><td><b>Code</b></td></tr><tr><td>*</td><td>Oral use <span style=\"background: LightGoldenRodYellow; margin: 4px; border: 1px solid khaki\"> (<a href=\"CodeSystem-routes-and-methods-of-administration-ema-cs.html\">Routes and Methods of Administration EMA</a>#100000073619)</span></td></tr></table></div>"
            },
            "status": "active",
            "formOf": [
              {
                "reference": "MedicinalProductDefinition/Norvasc-5mg-Tablet-SE-IS-MedicinalProductDefinition"
              }
            ],
            "administrableDoseForm": {
              "coding": [
                {
                  "system": "https://spor.ema.europa.eu/v1/lists/200000000004",
                  "code": "100000073664",
                  "display": "Tablet"
                }
              ]
            },
            "unitOfPresentation": {
              "coding": [
                {
                  "system": "https://spor.ema.europa.eu/v1/lists/200000000014",
                  "code": "200000002152",
                  "display": "Tablet"
                }
              ]
            },
            "producedFrom": [
              {
                "reference": "ManufacturedItemDefinition/Norvasc-5mg-Tablet-SE-IS-ManufacturedItemDefinition"
              }
            ],
            "routeOfAdministration": [
              {
                "code": {
                  "coding": [
                    {
                      "system": "https://spor.ema.europa.eu/v1/lists/100000073345",
                      "code": "100000073619",
                      "display": "Oral use"
                    }
                  ]
                }
              }
            ]
          },
          "search": {
            "mode": "match"
          }
        },
        {
          "fullUrl": "https://jpa.unicom.datawizard.it/fhir/AdministrableProductDefinition/Norvasc-10mg-Tablet-SE-IS-AdministrableProductDefinition",
          "resource": {
            "resourceType": "AdministrableProductDefinition",
            "id": "Norvasc-10mg-Tablet-SE-IS-AdministrableProductDefinition",
            "meta": {
              "versionId": "1",
              "lastUpdated": "2023-01-27T16:49:51.985+00:00",
              "source": "#GeHHfr7LNlngXCmI",
              "profile": [
                "http://unicom-project.eu/fhir/StructureDefinition/PPLAdministrableProductDefinition"
              ]
            },
            "text": {
              "status": "generated",
              "div": "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p><b>Generated Narrative: AdministrableProductDefinition</b><a name=\"Norvasc-10mg-Tablet-SE-IS-AdministrableProductDefinition\"> </a></p><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\">Resource AdministrableProductDefinition &quot;Norvasc-10mg-Tablet-SE-IS-AdministrableProductDefinition&quot; </p><p style=\"margin-bottom: 0px\">Profile: <a href=\"StructureDefinition-PPLAdministrableProductDefinition.html\">PPL Administrable Product profile</a></p></div><p><b>status</b>: active</p><p><b>formOf</b>: <a href=\"#MedicinalProductDefinition_Norvasc-10mg-Tablet-SE-IS-MedicinalProductDefinition\">See above (MedicinalProductDefinition/Norvasc-10mg-Tablet-SE-IS-MedicinalProductDefinition)</a></p><p><b>administrableDoseForm</b>: Tablet <span style=\"background: LightGoldenRodYellow; margin: 4px; border: 1px solid khaki\"> (<a href=\"CodeSystem-pharmaceutical-dose-form-ema-cs.html\">Pharmaceutical Dose Form EMA</a>#100000073664)</span></p><p><b>unitOfPresentation</b>: Tablet <span style=\"background: LightGoldenRodYellow; margin: 4px; border: 1px solid khaki\"> (<a href=\"CodeSystem-unit-of-presentation-ema-cs.html\">Unit of Presentation EMA</a>#200000002152)</span></p><p><b>producedFrom</b>: <a href=\"#ManufacturedItemDefinition_Norvasc-10mg-Tablet-SE-IS-ManufacturedItemDefinition\">See above (ManufacturedItemDefinition/Norvasc-10mg-Tablet-SE-IS-ManufacturedItemDefinition)</a></p><h3>RouteOfAdministrations</h3><table class=\"grid\"><tr><td>-</td><td><b>Code</b></td></tr><tr><td>*</td><td>Oral use <span style=\"background: LightGoldenRodYellow; margin: 4px; border: 1px solid khaki\"> (<a href=\"CodeSystem-routes-and-methods-of-administration-ema-cs.html\">Routes and Methods of Administration EMA</a>#100000073619)</span></td></tr></table></div>"
            },
            "status": "active",
            "formOf": [
              {
                "reference": "MedicinalProductDefinition/Norvasc-10mg-Tablet-SE-IS-MedicinalProductDefinition"
              }
            ],
            "administrableDoseForm": {
              "coding": [
                {
                  "system": "https://spor.ema.europa.eu/v1/lists/200000000004",
                  "code": "100000073664",
                  "display": "Tablet"
                }
              ]
            },
            "unitOfPresentation": {
              "coding": [
                {
                  "system": "https://spor.ema.europa.eu/v1/lists/200000000014",
                  "code": "200000002152",
                  "display": "Tablet"
                }
              ]
            },
            "producedFrom": [
              {
                "reference": "ManufacturedItemDefinition/Norvasc-10mg-Tablet-SE-IS-ManufacturedItemDefinition"
              }
            ],
            "routeOfAdministration": [
              {
                "code": {
                  "coding": [
                    {
                      "system": "https://spor.ema.europa.eu/v1/lists/100000073345",
                      "code": "100000073619",
                      "display": "Oral use"
                    }
                  ]
                }
              }
            ]
          },
          "search": {
            "mode": "match"
          }
        },
        {
          "fullUrl": "https://jpa.unicom.datawizard.it/fhir/AdministrableProductDefinition/LantusSolostar-EE-APD",
          "resource": {
            "resourceType": "AdministrableProductDefinition",
            "id": "LantusSolostar-EE-APD",
            "meta": {
              "versionId": "1",
              "lastUpdated": "2023-01-27T16:49:52.308+00:00",
              "source": "#UtXtW6aoPnfq12yk",
              "profile": [
                "http://unicom-project.eu/fhir/StructureDefinition/PPLAdministrableProductDefinition"
              ]
            },
            "text": {
              "status": "generated",
              "div": "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p><b>Generated Narrative: AdministrableProductDefinition</b><a name=\"LantusSolostar-EE-APD\"> </a></p><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\">Resource AdministrableProductDefinition &quot;LantusSolostar-EE-APD&quot; </p><p style=\"margin-bottom: 0px\">Profile: <a href=\"StructureDefinition-PPLAdministrableProductDefinition.html\">PPL Administrable Product profile</a></p></div><p><b>status</b>: active</p><p><b>formOf</b>: <a href=\"#MedicinalProductDefinition_LantusSolostar-EE-MPD\">See above (MedicinalProductDefinition/LantusSolostar-EE-MPD)</a></p><p><b>administrableDoseForm</b>: Solution for injection <span style=\"background: LightGoldenRodYellow; margin: 4px; border: 1px solid khaki\"> (<a href=\"CodeSystem-pharmaceutical-dose-form-ema-cs.html\">Pharmaceutical Dose Form EMA</a>#100000073863)</span></p><p><b>unitOfPresentation</b>: Pen <span style=\"background: LightGoldenRodYellow; margin: 4px; border: 1px solid khaki\"> (<a href=\"CodeSystem-unit-of-presentation-ema-cs.html\">Unit of Presentation EMA</a>#200000002135)</span></p><p><b>producedFrom</b>: <a href=\"#ManufacturedItemDefinition_LantusSolostar-EE-MID\">See above (ManufacturedItemDefinition/LantusSolostar-EE-MID)</a></p><h3>RouteOfAdministrations</h3><table class=\"grid\"><tr><td>-</td><td><b>Code</b></td></tr><tr><td>*</td><td>Subcutaneous use <span style=\"background: LightGoldenRodYellow; margin: 4px; border: 1px solid khaki\"> (<a href=\"CodeSystem-routes-and-methods-of-administration-ema-cs.html\">Routes and Methods of Administration EMA</a>#100000073633)</span></td></tr></table></div>"
            },
            "status": "active",
            "formOf": [
              {
                "reference": "MedicinalProductDefinition/LantusSolostar-EE-MPD"
              }
            ],
            "administrableDoseForm": {
              "coding": [
                {
                  "system": "https://spor.ema.europa.eu/v1/lists/200000000004",
                  "code": "100000073863",
                  "display": "Solution for injection"
                }
              ]
            },
            "unitOfPresentation": {
              "coding": [
                {
                  "system": "https://spor.ema.europa.eu/v1/lists/200000000014",
                  "code": "200000002135",
                  "display": "Pen"
                }
              ]
            },
            "producedFrom": [
              {
                "reference": "ManufacturedItemDefinition/LantusSolostar-EE-MID"
              }
            ],
            "routeOfAdministration": [
              {
                "code": {
                  "coding": [
                    {
                      "system": "https://spor.ema.europa.eu/v1/lists/100000073345",
                      "code": "100000073633",
                      "display": "Subcutaneous use"
                    }
                  ]
                }
              }
            ]
          },
          "search": {
            "mode": "match"
          }
        },
        {
          "fullUrl": "https://jpa.unicom.datawizard.it/fhir/AdministrableProductDefinition/CefuroximStragen-1.5g-Powder-SE-IS-AdminProdDef",
          "resource": {
            "resourceType": "AdministrableProductDefinition",
            "id": "CefuroximStragen-1.5g-Powder-SE-IS-AdminProdDef",
            "meta": {
              "versionId": "1",
              "lastUpdated": "2023-01-27T16:49:52.638+00:00",
              "source": "#ZOxvodbRkEPPTffK",
              "profile": [
                "http://unicom-project.eu/fhir/StructureDefinition/PPLAdministrableProductDefinition"
              ]
            },
            "text": {
              "status": "generated",
              "div": "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p><b>Generated Narrative: AdministrableProductDefinition</b><a name=\"CefuroximStragen-1.5g-Powder-SE-IS-AdminProdDef\"> </a></p><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\">Resource AdministrableProductDefinition &quot;CefuroximStragen-1.5g-Powder-SE-IS-AdminProdDef&quot; </p><p style=\"margin-bottom: 0px\">Profile: <a href=\"StructureDefinition-PPLAdministrableProductDefinition.html\">PPL Administrable Product profile</a></p></div><p><b>status</b>: active</p><p><b>formOf</b>: <a href=\"#MedicinalProductDefinition_CefuroximStragen-1.5g-Powder-SE-IS-MedicinalProductDefinition\">See above (MedicinalProductDefinition/CefuroximStragen-1.5g-Powder-SE-IS-MedicinalProductDefinition)</a></p><p><b>administrableDoseForm</b>: Solution for injection/infusion <span style=\"background: LightGoldenRodYellow; margin: 4px; border: 1px solid khaki\"> (<a href=\"CodeSystem-pharmaceutical-dose-form-ema-cs.html\">Pharmaceutical Dose Form EMA</a>#100000074038)</span></p><p><b>producedFrom</b>: <a href=\"#ManufacturedItemDefinition_CefuroximStragen-1.5g-Powder-SE-IS-ManufacturedItemDefinition\">See above (ManufacturedItemDefinition/CefuroximStragen-1.5g-Powder-SE-IS-ManufacturedItemDefinition)</a></p><h3>RouteOfAdministrations</h3><table class=\"grid\"><tr><td>-</td><td><b>Code</b></td></tr><tr><td>*</td><td>Intramuscular use <span style=\"background: LightGoldenRodYellow; margin: 4px; border: 1px solid khaki\"> (<a href=\"CodeSystem-routes-and-methods-of-administration-ema-cs.html\">Routes and Methods of Administration EMA</a>#100000073600; <a href=\"CodeSystem-routes-and-methods-of-administration-ema-cs.html\">Routes and Methods of Administration EMA</a>#100000073611 &quot;Intravenous use&quot;)</span></td></tr></table></div>"
            },
            "status": "active",
            "formOf": [
              {
                "reference": "MedicinalProductDefinition/CefuroximStragen-1.5g-Powder-SE-IS-MedicinalProductDefinition"
              }
            ],
            "administrableDoseForm": {
              "coding": [
                {
                  "system": "https://spor.ema.europa.eu/v1/lists/200000000004",
                  "code": "100000074038",
                  "display": "Solution for injection/infusion"
                }
              ]
            },
            "producedFrom": [
              {
                "reference": "ManufacturedItemDefinition/CefuroximStragen-1.5g-Powder-SE-IS-ManufacturedItemDefinition"
              }
            ],
            "routeOfAdministration": [
              {
                "code": {
                  "coding": [
                    {
                      "system": "https://spor.ema.europa.eu/v1/lists/100000073345",
                      "code": "100000073600",
                      "display": "Intramuscular use"
                    },
                    {
                      "system": "https://spor.ema.europa.eu/v1/lists/100000073345",
                      "code": "100000073611",
                      "display": "Intravenous use"
                    }
                  ]
                }
              }
            ]
          },
          "search": {
            "mode": "match"
          }
        },
        {
          "fullUrl": "https://jpa.unicom.datawizard.it/fhir/AdministrableProductDefinition/AMLteva-10mg-Tablet-SE-IS-AdministrableProductDefinition",
          "resource": {
            "resourceType": "AdministrableProductDefinition",
            "id": "AMLteva-10mg-Tablet-SE-IS-AdministrableProductDefinition",
            "meta": {
              "versionId": "1",
              "lastUpdated": "2023-01-27T16:49:52.866+00:00",
              "source": "#zlj0TD67b8xIVr4P",
              "profile": [
                "http://unicom-project.eu/fhir/StructureDefinition/PPLAdministrableProductDefinition"
              ]
            },
            "text": {
              "status": "generated",
              "div": "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p><b>Generated Narrative: AdministrableProductDefinition</b><a name=\"AMLteva-10mg-Tablet-SE-IS-AdministrableProductDefinition\"> </a></p><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\">Resource AdministrableProductDefinition &quot;AMLteva-10mg-Tablet-SE-IS-AdministrableProductDefinition&quot; </p><p style=\"margin-bottom: 0px\">Profile: <a href=\"StructureDefinition-PPLAdministrableProductDefinition.html\">PPL Administrable Product profile</a></p></div><p><b>status</b>: active</p><p><b>formOf</b>: <a href=\"#MedicinalProductDefinition_AMLteva-10mg-Tablet-SE-IS-MedicinalProductDefinition\">See above (MedicinalProductDefinition/AMLteva-10mg-Tablet-SE-IS-MedicinalProductDefinition)</a></p><p><b>administrableDoseForm</b>: Tablet <span style=\"background: LightGoldenRodYellow; margin: 4px; border: 1px solid khaki\"> (<a href=\"CodeSystem-pharmaceutical-dose-form-ema-cs.html\">Pharmaceutical Dose Form EMA</a>#100000073664)</span></p><p><b>unitOfPresentation</b>: Tablet <span style=\"background: LightGoldenRodYellow; margin: 4px; border: 1px solid khaki\"> (<a href=\"CodeSystem-unit-of-presentation-ema-cs.html\">Unit of Presentation EMA</a>#200000002152)</span></p><p><b>producedFrom</b>: <a href=\"#ManufacturedItemDefinition_AMLteva-10mg-Tablet-SE-IS-ManufacturedItemDefinition\">See above (ManufacturedItemDefinition/AMLteva-10mg-Tablet-SE-IS-ManufacturedItemDefinition)</a></p><h3>RouteOfAdministrations</h3><table class=\"grid\"><tr><td>-</td><td><b>Code</b></td></tr><tr><td>*</td><td>Oral use <span style=\"background: LightGoldenRodYellow; margin: 4px; border: 1px solid khaki\"> (<a href=\"CodeSystem-routes-and-methods-of-administration-ema-cs.html\">Routes and Methods of Administration EMA</a>#100000073619)</span></td></tr></table></div>"
            },
            "status": "active",
            "formOf": [
              {
                "reference": "MedicinalProductDefinition/AMLteva-10mg-Tablet-SE-IS-MedicinalProductDefinition"
              }
            ],
            "administrableDoseForm": {
              "coding": [
                {
                  "system": "https://spor.ema.europa.eu/v1/lists/200000000004",
                  "code": "100000073664",
                  "display": "Tablet"
                }
              ]
            },
            "unitOfPresentation": {
              "coding": [
                {
                  "system": "https://spor.ema.europa.eu/v1/lists/200000000014",
                  "code": "200000002152",
                  "display": "Tablet"
                }
              ]
            },
            "producedFrom": [
              {
                "reference": "ManufacturedItemDefinition/AMLteva-10mg-Tablet-SE-IS-ManufacturedItemDefinition"
              }
            ],
            "routeOfAdministration": [
              {
                "code": {
                  "coding": [
                    {
                      "system": "https://spor.ema.europa.eu/v1/lists/100000073345",
                      "code": "100000073619",
                      "display": "Oral use"
                    }
                  ]
                }
              }
            ]
          },
          "search": {
            "mode": "match"
          }
        },
        {
          "fullUrl": "https://jpa.unicom.datawizard.it/fhir/AdministrableProductDefinition/CanifugCremolum-10mg1g-Cream-EE-APD",
          "resource": {
            "resourceType": "AdministrableProductDefinition",
            "id": "CanifugCremolum-10mg1g-Cream-EE-APD",
            "meta": {
              "versionId": "1",
              "lastUpdated": "2023-01-27T16:49:53.162+00:00",
              "source": "#qc6iT30a1momSioH",
              "profile": [
                "http://unicom-project.eu/fhir/StructureDefinition/PPLAdministrableProductDefinition"
              ]
            },
            "text": {
              "status": "generated",
              "div": "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p><b>Generated Narrative: AdministrableProductDefinition</b><a name=\"CanifugCremolum-10mg1g-Cream-EE-APD\"> </a></p><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\">Resource AdministrableProductDefinition &quot;CanifugCremolum-10mg1g-Cream-EE-APD&quot; </p><p style=\"margin-bottom: 0px\">Profile: <a href=\"StructureDefinition-PPLAdministrableProductDefinition.html\">PPL Administrable Product profile</a></p></div><p><b>status</b>: active</p><p><b>formOf</b>: <a href=\"#MedicinalProductDefinition_CanifugCremolum-EE-MPD\">See above (MedicinalProductDefinition/CanifugCremolum-EE-MPD)</a></p><p><b>administrableDoseForm</b>: Cream <span style=\"background: LightGoldenRodYellow; margin: 4px; border: 1px solid khaki\"> (<a href=\"CodeSystem-pharmaceutical-dose-form-ema-cs.html\">Pharmaceutical Dose Form EMA</a>#100000073712)</span></p><p><b>unitOfPresentation</b>: Tube <span style=\"background: LightGoldenRodYellow; margin: 4px; border: 1px solid khaki\"> (<a href=\"CodeSystem-unit-of-presentation-ema-cs.html\">Unit of Presentation EMA</a>#200000002156)</span></p><p><b>producedFrom</b>: <a href=\"#ManufacturedItemDefinition_CanifugCremolum-10mg1g-Cream-EE-MID\">See above (ManufacturedItemDefinition/CanifugCremolum-10mg1g-Cream-EE-MID)</a></p><h3>RouteOfAdministrations</h3><table class=\"grid\"><tr><td>-</td><td><b>Code</b></td></tr><tr><td>*</td><td>Cutaneous use <span style=\"background: LightGoldenRodYellow; margin: 4px; border: 1px solid khaki\"> (<a href=\"CodeSystem-routes-and-methods-of-administration-ema-cs.html\">Routes and Methods of Administration EMA</a>#100000073566)</span></td></tr></table></div>"
            },
            "status": "active",
            "formOf": [
              {
                "reference": "MedicinalProductDefinition/CanifugCremolum-EE-MPD"
              }
            ],
            "administrableDoseForm": {
              "coding": [
                {
                  "system": "https://spor.ema.europa.eu/v1/lists/200000000004",
                  "code": "100000073712",
                  "display": "Cream"
                }
              ]
            },
            "unitOfPresentation": {
              "coding": [
                {
                  "system": "https://spor.ema.europa.eu/v1/lists/200000000014",
                  "code": "200000002156",
                  "display": "Tube"
                }
              ]
            },
            "producedFrom": [
              {
                "reference": "ManufacturedItemDefinition/CanifugCremolum-10mg1g-Cream-EE-MID"
              }
            ],
            "routeOfAdministration": [
              {
                "code": {
                  "coding": [
                    {
                      "system": "https://spor.ema.europa.eu/v1/lists/100000073345",
                      "code": "100000073566",
                      "display": "Cutaneous use"
                    }
                  ]
                }
              }
            ]
          },
          "search": {
            "mode": "match"
          }
        },
        {
          "fullUrl": "https://jpa.unicom.datawizard.it/fhir/AdministrableProductDefinition/CanifugCremolum-100mg-Pessary-EE-APD",
          "resource": {
            "resourceType": "AdministrableProductDefinition",
            "id": "CanifugCremolum-100mg-Pessary-EE-APD",
            "meta": {
              "versionId": "1",
              "lastUpdated": "2023-01-27T16:49:53.162+00:00",
              "source": "#qc6iT30a1momSioH",
              "profile": [
                "http://unicom-project.eu/fhir/StructureDefinition/PPLAdministrableProductDefinition"
              ]
            },
            "text": {
              "status": "generated",
              "div": "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p><b>Generated Narrative: AdministrableProductDefinition</b><a name=\"CanifugCremolum-100mg-Pessary-EE-APD\"> </a></p><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\">Resource AdministrableProductDefinition &quot;CanifugCremolum-100mg-Pessary-EE-APD&quot; </p><p style=\"margin-bottom: 0px\">Profile: <a href=\"StructureDefinition-PPLAdministrableProductDefinition.html\">PPL Administrable Product profile</a></p></div><p><b>status</b>: active</p><p><b>formOf</b>: <a href=\"#MedicinalProductDefinition_CanifugCremolum-EE-MPD\">See above (MedicinalProductDefinition/CanifugCremolum-EE-MPD)</a></p><p><b>administrableDoseForm</b>: Pessary <span style=\"background: LightGoldenRodYellow; margin: 4px; border: 1px solid khaki\"> (<a href=\"CodeSystem-pharmaceutical-dose-form-ema-cs.html\">Pharmaceutical Dose Form EMA</a>#100000073815)</span></p><p><b>unitOfPresentation</b>: Pessary <span style=\"background: LightGoldenRodYellow; margin: 4px; border: 1px solid khaki\"> (<a href=\"CodeSystem-unit-of-presentation-ema-cs.html\">Unit of Presentation EMA</a>#200000002137)</span></p><p><b>producedFrom</b>: <a href=\"#ManufacturedItemDefinition_CanifugCremolum-100mg-Pessary-EE-MID\">See above (ManufacturedItemDefinition/CanifugCremolum-100mg-Pessary-EE-MID)</a></p><h3>RouteOfAdministrations</h3><table class=\"grid\"><tr><td>-</td><td><b>Code</b></td></tr><tr><td>*</td><td>Vaginal use <span style=\"background: LightGoldenRodYellow; margin: 4px; border: 1px solid khaki\"> (<a href=\"CodeSystem-routes-and-methods-of-administration-ema-cs.html\">Routes and Methods of Administration EMA</a>#100000073639)</span></td></tr></table></div>"
            },
            "status": "active",
            "formOf": [
              {
                "reference": "MedicinalProductDefinition/CanifugCremolum-EE-MPD"
              }
            ],
            "administrableDoseForm": {
              "coding": [
                {
                  "system": "https://spor.ema.europa.eu/v1/lists/200000000004",
                  "code": "100000073815",
                  "display": "Pessary"
                }
              ]
            },
            "unitOfPresentation": {
              "coding": [
                {
                  "system": "https://spor.ema.europa.eu/v1/lists/200000000014",
                  "code": "200000002137",
                  "display": "Pessary"
                }
              ]
            },
            "producedFrom": [
              {
                "reference": "ManufacturedItemDefinition/CanifugCremolum-100mg-Pessary-EE-MID"
              }
            ],
            "routeOfAdministration": [
              {
                "code": {
                  "coding": [
                    {
                      "system": "https://spor.ema.europa.eu/v1/lists/100000073345",
                      "code": "100000073639",
                      "display": "Vaginal use"
                    }
                  ]
                }
              }
            ]
          },
          "search": {
            "mode": "match"
          }
        },
        {
          "fullUrl": "https://jpa.unicom.datawizard.it/fhir/AdministrableProductDefinition/AMLsandoz-5mg-Tablet-SE-IS-AdministrableProductDefinition",
          "resource": {
            "resourceType": "AdministrableProductDefinition",
            "id": "AMLsandoz-5mg-Tablet-SE-IS-AdministrableProductDefinition",
            "meta": {
              "versionId": "1",
              "lastUpdated": "2023-01-27T16:49:53.468+00:00",
              "source": "#4s6cR6fe0zcaOmvp",
              "profile": [
                "http://unicom-project.eu/fhir/StructureDefinition/PPLAdministrableProductDefinition"
              ]
            },
            "text": {
              "status": "generated",
              "div": "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p><b>Generated Narrative: AdministrableProductDefinition</b><a name=\"AMLsandoz-5mg-Tablet-SE-IS-AdministrableProductDefinition\"> </a></p><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\">Resource AdministrableProductDefinition &quot;AMLsandoz-5mg-Tablet-SE-IS-AdministrableProductDefinition&quot; </p><p style=\"margin-bottom: 0px\">Profile: <a href=\"StructureDefinition-PPLAdministrableProductDefinition.html\">PPL Administrable Product profile</a></p></div><p><b>status</b>: active</p><p><b>formOf</b>: <a href=\"#MedicinalProductDefinition_AMLsandoz-5mg-Tablet-SE-IS-MedicinalProductDefinition\">See above (MedicinalProductDefinition/AMLsandoz-5mg-Tablet-SE-IS-MedicinalProductDefinition)</a></p><p><b>administrableDoseForm</b>: Tablet <span style=\"background: LightGoldenRodYellow; margin: 4px; border: 1px solid khaki\"> (<a href=\"CodeSystem-pharmaceutical-dose-form-ema-cs.html\">Pharmaceutical Dose Form EMA</a>#100000073664)</span></p><p><b>unitOfPresentation</b>: Tablet <span style=\"background: LightGoldenRodYellow; margin: 4px; border: 1px solid khaki\"> (<a href=\"CodeSystem-unit-of-presentation-ema-cs.html\">Unit of Presentation EMA</a>#200000002152)</span></p><p><b>producedFrom</b>: <a href=\"#ManufacturedItemDefinition_AMLsandoz-5mg-Tablet-SE-IS-ManufacturedItemDefinition\">See above (ManufacturedItemDefinition/AMLsandoz-5mg-Tablet-SE-IS-ManufacturedItemDefinition)</a></p><h3>RouteOfAdministrations</h3><table class=\"grid\"><tr><td>-</td><td><b>Code</b></td></tr><tr><td>*</td><td>Oral use <span style=\"background: LightGoldenRodYellow; margin: 4px; border: 1px solid khaki\"> (<a href=\"CodeSystem-routes-and-methods-of-administration-ema-cs.html\">Routes and Methods of Administration EMA</a>#100000073619)</span></td></tr></table></div>"
            },
            "status": "active",
            "formOf": [
              {
                "reference": "MedicinalProductDefinition/AMLsandoz-5mg-Tablet-SE-IS-MedicinalProductDefinition"
              }
            ],
            "administrableDoseForm": {
              "coding": [
                {
                  "system": "https://spor.ema.europa.eu/v1/lists/200000000004",
                  "code": "100000073664",
                  "display": "Tablet"
                }
              ]
            },
            "unitOfPresentation": {
              "coding": [
                {
                  "system": "https://spor.ema.europa.eu/v1/lists/200000000014",
                  "code": "200000002152",
                  "display": "Tablet"
                }
              ]
            },
            "producedFrom": [
              {
                "reference": "ManufacturedItemDefinition/AMLsandoz-5mg-Tablet-SE-IS-ManufacturedItemDefinition"
              }
            ],
            "routeOfAdministration": [
              {
                "code": {
                  "coding": [
                    {
                      "system": "https://spor.ema.europa.eu/v1/lists/100000073345",
                      "code": "100000073619",
                      "display": "Oral use"
                    }
                  ]
                }
              }
            ]
          },
          "search": {
            "mode": "match"
          }
        },
        {
          "fullUrl": "https://jpa.unicom.datawizard.it/fhir/AdministrableProductDefinition/AMLteva-5mg-Tablet-SE-IS-AdministrableProductDefinition",
          "resource": {
            "resourceType": "AdministrableProductDefinition",
            "id": "AMLteva-5mg-Tablet-SE-IS-AdministrableProductDefinition",
            "meta": {
              "versionId": "1",
              "lastUpdated": "2023-01-27T16:49:53.815+00:00",
              "source": "#US0BMCcD8PaAeKf9",
              "profile": [
                "http://unicom-project.eu/fhir/StructureDefinition/PPLAdministrableProductDefinition"
              ]
            },
            "text": {
              "status": "generated",
              "div": "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p><b>Generated Narrative: AdministrableProductDefinition</b><a name=\"AMLteva-5mg-Tablet-SE-IS-AdministrableProductDefinition\"> </a></p><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\">Resource AdministrableProductDefinition &quot;AMLteva-5mg-Tablet-SE-IS-AdministrableProductDefinition&quot; </p><p style=\"margin-bottom: 0px\">Profile: <a href=\"StructureDefinition-PPLAdministrableProductDefinition.html\">PPL Administrable Product profile</a></p></div><p><b>status</b>: active</p><p><b>formOf</b>: <a href=\"#MedicinalProductDefinition_AMLteva-5mg-Tablet-SE-IS-MedicinalProductDefinition\">See above (MedicinalProductDefinition/AMLteva-5mg-Tablet-SE-IS-MedicinalProductDefinition)</a></p><p><b>administrableDoseForm</b>: Tablet <span style=\"background: LightGoldenRodYellow; margin: 4px; border: 1px solid khaki\"> (<a href=\"CodeSystem-pharmaceutical-dose-form-ema-cs.html\">Pharmaceutical Dose Form EMA</a>#100000073664)</span></p><p><b>unitOfPresentation</b>: Tablet <span style=\"background: LightGoldenRodYellow; margin: 4px; border: 1px solid khaki\"> (<a href=\"CodeSystem-unit-of-presentation-ema-cs.html\">Unit of Presentation EMA</a>#200000002152)</span></p><p><b>producedFrom</b>: <a href=\"#ManufacturedItemDefinition_AMLteva-5mg-Tablet-SE-IS-ManufacturedItemDefinition\">See above (ManufacturedItemDefinition/AMLteva-5mg-Tablet-SE-IS-ManufacturedItemDefinition)</a></p><h3>RouteOfAdministrations</h3><table class=\"grid\"><tr><td>-</td><td><b>Code</b></td></tr><tr><td>*</td><td>Oral use <span style=\"background: LightGoldenRodYellow; margin: 4px; border: 1px solid khaki\"> (<a href=\"CodeSystem-routes-and-methods-of-administration-ema-cs.html\">Routes and Methods of Administration EMA</a>#100000073619)</span></td></tr></table></div>"
            },
            "status": "active",
            "formOf": [
              {
                "reference": "MedicinalProductDefinition/AMLteva-5mg-Tablet-SE-IS-MedicinalProductDefinition"
              }
            ],
            "administrableDoseForm": {
              "coding": [
                {
                  "system": "https://spor.ema.europa.eu/v1/lists/200000000004",
                  "code": "100000073664",
                  "display": "Tablet"
                }
              ]
            },
            "unitOfPresentation": {
              "coding": [
                {
                  "system": "https://spor.ema.europa.eu/v1/lists/200000000014",
                  "code": "200000002152",
                  "display": "Tablet"
                }
              ]
            },
            "producedFrom": [
              {
                "reference": "ManufacturedItemDefinition/AMLteva-5mg-Tablet-SE-IS-ManufacturedItemDefinition"
              }
            ],
            "routeOfAdministration": [
              {
                "code": {
                  "coding": [
                    {
                      "system": "https://spor.ema.europa.eu/v1/lists/100000073345",
                      "code": "100000073619",
                      "display": "Oral use"
                    }
                  ]
                }
              }
            ]
          },
          "search": {
            "mode": "match"
          }
        },
        {
          "fullUrl": "https://jpa.unicom.datawizard.it/fhir/AdministrableProductDefinition/Hipres-10mg-Tablet-EE-APD",
          "resource": {
            "resourceType": "AdministrableProductDefinition",
            "id": "Hipres-10mg-Tablet-EE-APD",
            "meta": {
              "versionId": "1",
              "lastUpdated": "2023-01-27T16:49:54.124+00:00",
              "source": "#vZLvgOoZThx5vSpd",
              "profile": [
                "http://unicom-project.eu/fhir/StructureDefinition/PPLAdministrableProductDefinition"
              ]
            },
            "text": {
              "status": "generated",
              "div": "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p><b>Generated Narrative: AdministrableProductDefinition</b><a name=\"Hipres-10mg-Tablet-EE-APD\"> </a></p><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\">Resource AdministrableProductDefinition &quot;Hipres-10mg-Tablet-EE-APD&quot; </p><p style=\"margin-bottom: 0px\">Profile: <a href=\"StructureDefinition-PPLAdministrableProductDefinition.html\">PPL Administrable Product profile</a></p></div><p><b>status</b>: active</p><p><b>formOf</b>: <a href=\"#MedicinalProductDefinition_Hipres-10mg-Tablet-EE-MPD\">See above (MedicinalProductDefinition/Hipres-10mg-Tablet-EE-MPD)</a></p><p><b>administrableDoseForm</b>: Tablet <span style=\"background: LightGoldenRodYellow; margin: 4px; border: 1px solid khaki\"> (<a href=\"CodeSystem-pharmaceutical-dose-form-ema-cs.html\">Pharmaceutical Dose Form EMA</a>#100000073664)</span></p><p><b>producedFrom</b>: <a href=\"#ManufacturedItemDefinition_Hipres-10mg-Tablet-EE-MID\">See above (ManufacturedItemDefinition/Hipres-10mg-Tablet-EE-MID)</a></p><h3>RouteOfAdministrations</h3><table class=\"grid\"><tr><td>-</td><td><b>Code</b></td></tr><tr><td>*</td><td>Oral use <span style=\"background: LightGoldenRodYellow; margin: 4px; border: 1px solid khaki\"> (<a href=\"CodeSystem-routes-and-methods-of-administration-ema-cs.html\">Routes and Methods of Administration EMA</a>#100000073619)</span></td></tr></table></div>"
            },
            "status": "active",
            "formOf": [
              {
                "reference": "MedicinalProductDefinition/Hipres-10mg-Tablet-EE-MPD"
              }
            ],
            "administrableDoseForm": {
              "coding": [
                {
                  "system": "https://spor.ema.europa.eu/v1/lists/200000000004",
                  "code": "100000073664",
                  "display": "Tablet"
                }
              ]
            },
            "producedFrom": [
              {
                "reference": "ManufacturedItemDefinition/Hipres-10mg-Tablet-EE-MID"
              }
            ],
            "routeOfAdministration": [
              {
                "code": {
                  "coding": [
                    {
                      "system": "https://spor.ema.europa.eu/v1/lists/100000073345",
                      "code": "100000073619",
                      "display": "Oral use"
                    }
                  ]
                }
              }
            ]
          },
          "search": {
            "mode": "match"
          }
        },
        {
          "fullUrl": "https://jpa.unicom.datawizard.it/fhir/AdministrableProductDefinition/Clexane-60mg-0.6ml-solinj-EE-APD",
          "resource": {
            "resourceType": "AdministrableProductDefinition",
            "id": "Clexane-60mg-0.6ml-solinj-EE-APD",
            "meta": {
              "versionId": "1",
              "lastUpdated": "2023-01-27T16:49:54.411+00:00",
              "source": "#DdxUQSvia6CnCqcq",
              "profile": [
                "http://unicom-project.eu/fhir/StructureDefinition/PPLAdministrableProductDefinition"
              ]
            },
            "text": {
              "status": "generated",
              "div": "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p><b>Generated Narrative: AdministrableProductDefinition</b><a name=\"Clexane-60mg-0.6ml-solinj-EE-APD\"> </a></p><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\">Resource AdministrableProductDefinition &quot;Clexane-60mg-0.6ml-solinj-EE-APD&quot; </p><p style=\"margin-bottom: 0px\">Profile: <a href=\"StructureDefinition-PPLAdministrableProductDefinition.html\">PPL Administrable Product profile</a></p></div><p><b>status</b>: active</p><p><b>formOf</b>: <a href=\"#MedicinalProductDefinition_Clexane-60mg-0.6ml-solinj-EE-MPD\">See above (MedicinalProductDefinition/Clexane-60mg-0.6ml-solinj-EE-MPD)</a></p><p><b>administrableDoseForm</b>: Solution for injection <span style=\"background: LightGoldenRodYellow; margin: 4px; border: 1px solid khaki\"> (<a href=\"CodeSystem-pharmaceutical-dose-form-ema-cs.html\">Pharmaceutical Dose Form EMA</a>#100000073863)</span></p><p><b>unitOfPresentation</b>: Syringe <span style=\"background: LightGoldenRodYellow; margin: 4px; border: 1px solid khaki\"> (<a href=\"CodeSystem-unit-of-presentation-ema-cs.html\">Unit of Presentation EMA</a>#200000002150)</span></p><p><b>producedFrom</b>: <a href=\"#ManufacturedItemDefinition_Clexane-60mg-0.6ml-solinj-EE-MID\">See above (ManufacturedItemDefinition/Clexane-60mg-0.6ml-solinj-EE-MID)</a></p><h3>RouteOfAdministrations</h3><table class=\"grid\"><tr><td>-</td><td><b>Code</b></td></tr><tr><td>*</td><td>Subcutaneous use <span style=\"background: LightGoldenRodYellow; margin: 4px; border: 1px solid khaki\"> (<a href=\"CodeSystem-routes-and-methods-of-administration-ema-cs.html\">Routes and Methods of Administration EMA</a>#100000073633)</span></td></tr></table></div>"
            },
            "status": "active",
            "formOf": [
              {
                "reference": "MedicinalProductDefinition/Clexane-60mg-0.6ml-solinj-EE-MPD"
              }
            ],
            "administrableDoseForm": {
              "coding": [
                {
                  "system": "https://spor.ema.europa.eu/v1/lists/200000000004",
                  "code": "100000073863",
                  "display": "Solution for injection"
                }
              ]
            },
            "unitOfPresentation": {
              "coding": [
                {
                  "system": "https://spor.ema.europa.eu/v1/lists/200000000014",
                  "code": "200000002150",
                  "display": "Syringe"
                }
              ]
            },
            "producedFrom": [
              {
                "reference": "ManufacturedItemDefinition/Clexane-60mg-0.6ml-solinj-EE-MID"
              }
            ],
            "routeOfAdministration": [
              {
                "code": {
                  "coding": [
                    {
                      "system": "https://spor.ema.europa.eu/v1/lists/100000073345",
                      "code": "100000073633",
                      "display": "Subcutaneous use"
                    }
                  ]
                }
              }
            ]
          },
          "search": {
            "mode": "match"
          }
        },
        {
          "fullUrl": "https://jpa.unicom.datawizard.it/fhir/AdministrableProductDefinition/AMLvitabalans-10mg-Tablet-SE-IS-AdministrableProductDefinition",
          "resource": {
            "resourceType": "AdministrableProductDefinition",
            "id": "AMLvitabalans-10mg-Tablet-SE-IS-AdministrableProductDefinition",
            "meta": {
              "versionId": "1",
              "lastUpdated": "2023-01-27T16:49:54.580+00:00",
              "source": "#RFniaZnPtbPEbpSv",
              "profile": [
                "http://unicom-project.eu/fhir/StructureDefinition/PPLAdministrableProductDefinition"
              ]
            },
            "text": {
              "status": "generated",
              "div": "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p><b>Generated Narrative: AdministrableProductDefinition</b><a name=\"AMLvitabalans-10mg-Tablet-SE-IS-AdministrableProductDefinition\"> </a></p><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\">Resource AdministrableProductDefinition &quot;AMLvitabalans-10mg-Tablet-SE-IS-AdministrableProductDefinition&quot; </p><p style=\"margin-bottom: 0px\">Profile: <a href=\"StructureDefinition-PPLAdministrableProductDefinition.html\">PPL Administrable Product profile</a></p></div><p><b>status</b>: active</p><p><b>formOf</b>: <a href=\"#MedicinalProductDefinition_AMLvitabalans-10mg-Tablet-SE-IS-MedicinalProductDefinition\">See above (MedicinalProductDefinition/AMLvitabalans-10mg-Tablet-SE-IS-MedicinalProductDefinition)</a></p><p><b>administrableDoseForm</b>: Tablet <span style=\"background: LightGoldenRodYellow; margin: 4px; border: 1px solid khaki\"> (<a href=\"CodeSystem-pharmaceutical-dose-form-ema-cs.html\">Pharmaceutical Dose Form EMA</a>#100000073664)</span></p><p><b>unitOfPresentation</b>: Tablet <span style=\"background: LightGoldenRodYellow; margin: 4px; border: 1px solid khaki\"> (<a href=\"CodeSystem-unit-of-presentation-ema-cs.html\">Unit of Presentation EMA</a>#200000002152)</span></p><p><b>producedFrom</b>: <a href=\"#ManufacturedItemDefinition_AMLvitabalans-10mg-Tablet-SE-IS-ManufacturedItemDefinition\">See above (ManufacturedItemDefinition/AMLvitabalans-10mg-Tablet-SE-IS-ManufacturedItemDefinition)</a></p><h3>RouteOfAdministrations</h3><table class=\"grid\"><tr><td>-</td><td><b>Code</b></td></tr><tr><td>*</td><td>Oral use <span style=\"background: LightGoldenRodYellow; margin: 4px; border: 1px solid khaki\"> (<a href=\"CodeSystem-routes-and-methods-of-administration-ema-cs.html\">Routes and Methods of Administration EMA</a>#100000073619)</span></td></tr></table></div>"
            },
            "status": "active",
            "formOf": [
              {
                "reference": "MedicinalProductDefinition/AMLvitabalans-10mg-Tablet-SE-IS-MedicinalProductDefinition"
              }
            ],
            "administrableDoseForm": {
              "coding": [
                {
                  "system": "https://spor.ema.europa.eu/v1/lists/200000000004",
                  "code": "100000073664",
                  "display": "Tablet"
                }
              ]
            },
            "unitOfPresentation": {
              "coding": [
                {
                  "system": "https://spor.ema.europa.eu/v1/lists/200000000014",
                  "code": "200000002152",
                  "display": "Tablet"
                }
              ]
            },
            "producedFrom": [
              {
                "reference": "ManufacturedItemDefinition/AMLvitabalans-10mg-Tablet-SE-IS-ManufacturedItemDefinition"
              }
            ],
            "routeOfAdministration": [
              {
                "code": {
                  "coding": [
                    {
                      "system": "https://spor.ema.europa.eu/v1/lists/100000073345",
                      "code": "100000073619",
                      "display": "Oral use"
                    }
                  ]
                }
              }
            ]
          },
          "search": {
            "mode": "match"
          }
        },
        {
          "fullUrl": "https://jpa.unicom.datawizard.it/fhir/AdministrableProductDefinition/AMLaccord-10mg-Tablet-SE-IS-AdministrableProductDefinition",
          "resource": {
            "resourceType": "AdministrableProductDefinition",
            "id": "AMLaccord-10mg-Tablet-SE-IS-AdministrableProductDefinition",
            "meta": {
              "versionId": "1",
              "lastUpdated": "2023-01-27T16:49:54.797+00:00",
              "source": "#dhfIOezA2Hrnj7CP",
              "profile": [
                "http://unicom-project.eu/fhir/StructureDefinition/PPLAdministrableProductDefinition"
              ]
            },
            "text": {
              "status": "generated",
              "div": "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p><b>Generated Narrative: AdministrableProductDefinition</b><a name=\"AMLaccord-10mg-Tablet-SE-IS-AdministrableProductDefinition\"> </a></p><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\">Resource AdministrableProductDefinition &quot;AMLaccord-10mg-Tablet-SE-IS-AdministrableProductDefinition&quot; </p><p style=\"margin-bottom: 0px\">Profile: <a href=\"StructureDefinition-PPLAdministrableProductDefinition.html\">PPL Administrable Product profile</a></p></div><p><b>status</b>: active</p><p><b>formOf</b>: <a href=\"#MedicinalProductDefinition_AMLaccord-10mg-Tablet-SE-IS-MedicinalProductDefinition\">See above (MedicinalProductDefinition/AMLaccord-10mg-Tablet-SE-IS-MedicinalProductDefinition)</a></p><p><b>administrableDoseForm</b>: Tablet <span style=\"background: LightGoldenRodYellow; margin: 4px; border: 1px solid khaki\"> (<a href=\"CodeSystem-pharmaceutical-dose-form-ema-cs.html\">Pharmaceutical Dose Form EMA</a>#100000073664)</span></p><p><b>unitOfPresentation</b>: Tablet <span style=\"background: LightGoldenRodYellow; margin: 4px; border: 1px solid khaki\"> (<a href=\"CodeSystem-unit-of-presentation-ema-cs.html\">Unit of Presentation EMA</a>#200000002152)</span></p><p><b>producedFrom</b>: <a href=\"#ManufacturedItemDefinition_AMLaccord-10mg-Tablet-SE-IS-ManufacturedItemDefinition\">See above (ManufacturedItemDefinition/AMLaccord-10mg-Tablet-SE-IS-ManufacturedItemDefinition)</a></p><h3>RouteOfAdministrations</h3><table class=\"grid\"><tr><td>-</td><td><b>Code</b></td></tr><tr><td>*</td><td>Oral use <span style=\"background: LightGoldenRodYellow; margin: 4px; border: 1px solid khaki\"> (<a href=\"CodeSystem-routes-and-methods-of-administration-ema-cs.html\">Routes and Methods of Administration EMA</a>#100000073619)</span></td></tr></table></div>"
            },
            "status": "active",
            "formOf": [
              {
                "reference": "MedicinalProductDefinition/AMLaccord-10mg-Tablet-SE-IS-MedicinalProductDefinition"
              }
            ],
            "administrableDoseForm": {
              "coding": [
                {
                  "system": "https://spor.ema.europa.eu/v1/lists/200000000004",
                  "code": "100000073664",
                  "display": "Tablet"
                }
              ]
            },
            "unitOfPresentation": {
              "coding": [
                {
                  "system": "https://spor.ema.europa.eu/v1/lists/200000000014",
                  "code": "200000002152",
                  "display": "Tablet"
                }
              ]
            },
            "producedFrom": [
              {
                "reference": "ManufacturedItemDefinition/AMLaccord-10mg-Tablet-SE-IS-ManufacturedItemDefinition"
              }
            ],
            "routeOfAdministration": [
              {
                "code": {
                  "coding": [
                    {
                      "system": "https://spor.ema.europa.eu/v1/lists/100000073345",
                      "code": "100000073619",
                      "display": "Oral use"
                    }
                  ]
                }
              }
            ]
          },
          "search": {
            "mode": "match"
          }
        }
      ]
    }