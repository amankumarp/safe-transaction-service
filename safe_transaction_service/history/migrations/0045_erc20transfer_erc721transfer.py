# Generated by Django 3.2.8 on 2021-10-29 11:13

import django.db.models.deletion
from django.db import migrations, models

import gnosis.eth.django.models


class Migration(migrations.Migration):

    dependencies = [
        ("history", "0044_reprocess_module_txs"),
    ]

    operations = [
        migrations.CreateModel(
            name="ERC20Transfer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "address",
                    gnosis.eth.django.models.EthereumAddressField(db_index=True),
                ),
                ("_from", gnosis.eth.django.models.EthereumAddressField(db_index=True)),
                ("to", gnosis.eth.django.models.EthereumAddressField(db_index=True)),
                ("log_index", models.PositiveIntegerField()),
                ("value", gnosis.eth.django.models.Uint256Field()),
                (
                    "ethereum_tx",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="history.ethereumtx",
                    ),
                ),
            ],
            options={
                "verbose_name": "ERC20 Transfer",
                "verbose_name_plural": "ERC20 Transfers",
            },
        ),
        migrations.CreateModel(
            name="ERC721Transfer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "address",
                    gnosis.eth.django.models.EthereumAddressField(db_index=True),
                ),
                ("_from", gnosis.eth.django.models.EthereumAddressField(db_index=True)),
                ("to", gnosis.eth.django.models.EthereumAddressField(db_index=True)),
                ("log_index", models.PositiveIntegerField()),
                ("token_id", gnosis.eth.django.models.Uint256Field()),
                (
                    "ethereum_tx",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="history.ethereumtx",
                    ),
                ),
            ],
            options={
                "verbose_name": "ERC721 Transfer",
                "verbose_name_plural": "ERC721 Transfers",
            },
        ),
        migrations.RunSQL(
            """
            INSERT INTO history_erc20transfer(address, ethereum_tx_id, "_from", "to", log_index, value)
            SELECT address, ethereum_tx_id, arguments->>'from', arguments->>'to', log_index, (arguments->>'value')::numeric
            FROM history_ethereumevent WHERE arguments ? 'value'
            """
        ),
        migrations.RunSQL(
            """
            INSERT INTO history_erc721transfer(address, ethereum_tx_id, "_from", "to", log_index, token_id)
            SELECT address, ethereum_tx_id, arguments->>'from', arguments->>'to', log_index, (arguments->>'tokenId')::numeric
            FROM history_ethereumevent WHERE arguments ? 'tokenId'
            """
        ),
    ]