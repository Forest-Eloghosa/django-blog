from django.db import migrations


def create_default_about(apps, schema_editor):
    About = apps.get_model('about', 'About')
    if About.objects.exists():
        return

    About.objects.create(
        title='About CodeStar',
        content=(
            "<p>Hi — I’m Forest, and this is CodeStar, my little corner for practical developer notes. "
            "I write about the kinds of problems I actually solve: Django migrations, Git workflows, "
            "deployment gotchas, and accessibility improvements. My goal is to give you clear, repeatable "
            "steps so you can fix the same problems quickly in your projects.</p>"
            "<p>Expect hands-on walkthroughs, small scripts to automate setup, and short posts that pair "
            "code with a plain-English explanation. If you like the examples here, check the CONTRIBUTING.md "
            "and the scripts folder to get your local copy running fast.</p>"
        ),
    )


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_default_about, reverse_code=migrations.RunPython.noop),
    ]
