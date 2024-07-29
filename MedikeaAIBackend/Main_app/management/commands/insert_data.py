from django.core.management.base import BaseCommand
from Main_app.models import *
from .Data import *


class Command(BaseCommand):
    help = 'Insert initial data to be seeded'

    def handle(self, *args, **kwargs):
        # provisional_experts_levels = metadata['provisional_experts_levels']
        # service_provision_level = metadata['service_provision_level']
        diseases = metadata['diseases']

        # for expert in provisional_experts_levels:
        #     expert_obj = ProfessionalExpertise.objects.get_or_create(name=expert['name'])
        #     expert_obj = expert_obj[0]
        #     for level in expert['Level']:
        #         level_obj = ServiceLevel.objects.get_or_create(name=level)
        #         level = level_obj[0]
        #         expert_obj.levels.add(level)
        #         expert_obj.save()
        # self.stdout.write(self.style.SUCCESS('Successfully seeded data for provisional experts'))

        # for service_level in service_provision_level:
        #     service_level_obj = ServiceProvision.objects.get_or_create(name=service_level['name'])
        #     service_obj = service_level_obj[0]
        #     for level in service_level['Level']:
        #         level_obj = ServiceLevel.objects.get_or_create(name=level)
        #         level = level_obj[0]
        #         service_obj.levels.add(level)
        #         service_obj.save()
        # self.stdout.write(self.style.SUCCESS('Successfully seeded data for service provision'))

        # recived_drugs_json = all_drugs
        # for drug in recived_drugs_json:
        #     category_name = drug['name']
        #     category_obj = DrugCategory.objects.get_or_create(name=category_name)
        #     category_obj = category_obj[0]

        #     subcategories = []
        #     try:
        #         subcategories = drug['subcategories']
        #     except:
        #         pass

        #     if len(subcategories) > 0:
        #         for subcategory in subcategories:
        #             subcategory_name = subcategory['name']
        #             subcategory_items = []
        #             try:
        #                 subcategory_items = subcategory['items']
        #             except:
        #                 pass
        #             # subcategory_items = subcategory['items']

        #             if len(subcategory_items) > 0:
        #                 for item in subcategory_items:
        #                     service_level_name = item['level']
        #                     service_level_obj = ServiceLevel.objects.get_or_create(name=service_level_name)
        #                     service_level_obj = service_level_obj[0]

        #                     drug_item_obj = Drugstore.objects.get_or_create(name=item['name'], dosage_form=item['dosage_form'], strength = item['strength'], level = service_level_obj, sub_categories = subcategory_name, drug_category = category_obj)

        # self.stdout.write(self.style.SUCCESS('Successfully seeded data for recived drugs'))

        diseases_json = diseases
        for disease in diseases_json:
            description = disease.get('description', '')
            notes = disease.get('notes', [])
            disease_obj = Disease.objects.get_or_create(name=disease['name'], description=description, notes = notes)
            indications = disease.get('indications', [])
            if indications:
                disease = disease_obj[0]
                disease.indications = indications
                disease.save() 
            disease_obj = disease_obj[0]
            clinical_presentation= disease.get('clinical_presentation', [])
            
            investigations = disease.get('investigations', [])
            treatments = disease.get('treatments', [])
            clinical_presentation_arr = []
            if len(clinical_presentation) >0:
                for presentation in clinical_presentation:
                    try:
                        clinical_presentation_split = presentation.split(',')
                        for clinical_presentation_split_item in clinical_presentation_split:
                            clinical_presentation_arr.append(clinical_presentation_split_item)
                    except:
                        clinical_presentation_arr.append(clinical_presentation)

            if len(clinical_presentation_arr) > 0:
                for presentation in clinical_presentation_arr:
                    presentation_obj = Symptom.objects.get_or_create(name=presentation)
                    presentation_obj = presentation_obj[0]
                    disease_obj.symptoms.add(presentation_obj)

            if len(investigations) > 0:
                for investigation in investigations:
                    investigation_obj = Investigation.objects.get_or_create(name=investigation)
                    investigation_obj = investigation_obj[0]
                    disease_obj.investigations.add(investigation_obj)

            if len(treatments) > 0:
                for treatment in treatments:
                    treatment_category_name_arr = []
                    try:
                        treatment_category_name_arr = treatment.keys()
                    except:
                        pass
                    
                    if len(treatment_category_name_arr) >0:
                        for treatment_category_name in treatment_category_name_arr:
                            treatment_category = TeatmentCategory.objects.get_or_create(name=treatment_category_name)
                            treatment_category = treatment_category[0]
                            if treatment_category_name == 'Non-Pharmacological Treatment':
                                treatment_category_detail_name_arr = treatment[treatment_category_name]
                                for treatment_category_detail_name in treatment_category_detail_name_arr:
                                    for causes, recommendations in treatment_category_detail_name.items():
                                        treatment_obj = Treatment.objects.get_or_create(name=causes, treatment_category = treatment_category, recommendations= recommendations)
                                        treatment_obj = treatment_obj[0]
                                        disease_obj.treatment.add(treatment_obj)
                            if treatment_category_name == 'Pharmacological Treatment':
                                treatment_category_detail_name_arr = treatment[treatment_category_name]
                                for treatment_category_detail_name in treatment_category_detail_name_arr:
                                    print('ok')
                                    # drug_obj =Drugstore.objects.get_or_create(name=treatment_category_detail_name)['name']
                                    # pharmacologilical_treatment_obj = PharmacologicalTreatment.objects.get_or_create(name=treatment_category_detail_name)


        self.stdout.write(self.style.SUCCESS('Successfully seeded data for disease information'))
