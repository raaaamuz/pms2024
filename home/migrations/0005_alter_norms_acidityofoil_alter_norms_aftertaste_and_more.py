# Generated by Django 5.0.2 on 2024-03-06 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_norms_delete_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='norms',
            name='acidityofoil',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='aftertaste',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='appearance',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='aromaorsmell',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='aromaorsmellaftermixingwithsalad',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='aromasmell',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='attractivedesign',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='attractiveorlikepackcolour',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='attractiveshapeorlikeshape',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='believability',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='bitterness',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='bodyorvolumeofhairpostwashing',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='bounceofhairpostwashing',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='burningorscarringofscalpduetotheproductapplied',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='carbonation',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='cheesetaste',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='color',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='colour',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='colourofhairpostwashing',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='comfortonfingers',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='comprehension',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='concept_uniqueness',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='concept_valueformoney',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='convenienttouse',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='creaminess',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='creamytaste',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='creamytexture',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='crispiness',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='doesnotirritateorstingoritch',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='easeoffixing',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='easeofgripping',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='easeofholding',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='easeofmixingduringfoodpreparation',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='easeofoplaiting',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='easeofsplitting',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='easeofspreading',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='easeoftrimming',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='efficacyoftheproduct',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='elegantlook',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='extentoftangingduringcombing',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='extentoftangingduringfixing',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='eyecatching',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='fattiness',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='firmness',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='flavor',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='freshingredients',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='freshness',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='freshtaste',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='genderofrespondent',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='goodqualitymaterial',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='hairfallwhileapplying',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='hairfallwhilewashingofftheproduct',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='hairstrengthafterwashingofftheproduct',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='heavinessofbraids',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='indulgingtaste',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='innovativedesign',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='lightness',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='likelihoodtorecommend',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='liking',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='mildorgentle',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='milkiness',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='milkyaroma',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='modernorcontemporarylook',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='mouthfeel',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='mouthfeeloffruitpieces',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='naturalsaltiness',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='naturalsweetness',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='naturaltaste',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='naturaltasteoffruitpieces',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='neatnessofplaits',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='oiliness',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='overallattractiveness',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='overallopinion',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='overallopiniononfinallook',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='overalltimetakenintheentireprocess',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='pack_relevance',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='pack_uniqueness',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='pack_valueformoney',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='pourability',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='premiumlook',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='purchaseintentionpriced',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='purchaseintentionunpriced',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='qtyoffruitpieces',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='qualityofpotato',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='quantityinsinglepack',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='relevance',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='relevanceoverall',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='safetouse',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='saltiness',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='secnew',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='shine',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='shineofbraids',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='shineofhairextension',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='shineofhairpostwashing',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='size',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='sizeoffruitpieces',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='smellorfragrance',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='smoothness',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='smoothnessofbraids',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='smoothnessofhairextension',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='softnessofbraids',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='softnessofhairextension',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='sourness',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='spreadability',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='stickiness',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='stomachfeel',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='straighteningofhairpostwashing',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='strengthofhairextension',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='suitableforinhomeuse',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='suitableforoutofhomeuse',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='sweetness',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='taste',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='tastegoodforbreakfast',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='tasteofenddish',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='tasteoffruitpieces',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='tasteofmilk',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='tasterichincream',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='texture',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='textureorconsistency',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='thickness',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='thicknessofbraids',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='thicknessorconsistency',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='traditionallook',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='uniqueness',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='valueformoney',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='wellsealed',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='norms',
            name='wouldstandoutonshelf',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
