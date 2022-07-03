from django.db import models


class adjazenzmatrix_variablen(models.Model):
    index = models.TextField(primary_key=True, blank=True)
    bl_eintragetemp = models.BigIntegerField(db_column='BL_EINTRAGETEMP', blank=True, null=True)
    co_kvz = models.BigIntegerField(db_column='CO_KVZ', blank=True, null=True)
    f_gas_z1 = models.BigIntegerField(db_column='F_GAS_Z1', blank=True, null=True)
    f_gas_z2 = models.BigIntegerField(db_column='F_GAS_Z2', blank=True, null=True)
    f_gas_z3 = models.BigIntegerField(db_column='F_GAS_Z3', blank=True, null=True)
    f_gas_z4 = models.BigIntegerField(db_column='F_GAS_Z4', blank=True, null=True)
    f_luft_z1 = models.BigIntegerField(db_column='F_LUFT_Z1', blank=True, null=True)
    f_luft_z2 = models.BigIntegerField(db_column='F_LUFT_Z2', blank=True, null=True)
    f_luft_z3 = models.BigIntegerField(db_column='F_LUFT_Z3', blank=True, null=True)
    f_luft_z4 = models.BigIntegerField(db_column='F_LUFT_Z4', blank=True, null=True)
    o2_kvz = models.BigIntegerField(db_column='O2_KVZ', blank=True, null=True)
    o2_nach_reku = models.BigIntegerField(db_column='O2_NACH_REKU', blank=True, null=True)
    o2_vor_reku = models.BigIntegerField(db_column='O2_VOR_REKU', blank=True, null=True)
    o2_zone1 = models.BigIntegerField(db_column='O2_ZONE1', blank=True, null=True)
    o2_zone2 = models.BigIntegerField(db_column='O2_ZONE2', blank=True, null=True)
    o2_zone3 = models.BigIntegerField(db_column='O2_ZONE3', blank=True, null=True)
    o2_zone4 = models.BigIntegerField(db_column='O2_ZONE4', blank=True, null=True)
    ofenraumdruck_zone_1 = models.BigIntegerField(db_column='OFENRAUMDRUCK_ZONE_1', blank=True, null=True)
    ofenraumdruck_zone_2 = models.BigIntegerField(db_column='OFENRAUMDRUCK_ZONE_2', blank=True, null=True)
    ofenraumdruck_zone_3 = models.BigIntegerField(db_column='OFENRAUMDRUCK_ZONE_3', blank=True, null=True)
    ofenraumdruck_zone_4 = models.BigIntegerField(db_column='OFENRAUMDRUCK_ZONE_4', blank=True, null=True)
    status_betrieb_zone_1 = models.BigIntegerField(db_column='STATUS_BETRIEB_ZONE_1', blank=True, null=True)
    status_betrieb_zone_2 = models.BigIntegerField(db_column='STATUS_BETRIEB_ZONE_2', blank=True, null=True)
    status_betrieb_zone_3 = models.BigIntegerField(db_column='STATUS_BETRIEB_ZONE_3', blank=True, null=True)
    status_betrieb_zone_4 = models.BigIntegerField(db_column='STATUS_BETRIEB_ZONE_4', blank=True, null=True)
    status_strasse = models.BigIntegerField(db_column='STATUS_STRASSE', blank=True, null=True)
    status_zone_1 = models.BigIntegerField(db_column='STATUS_ZONE_1', blank=True, null=True)
    status_zone_2 = models.BigIntegerField(db_column='STATUS_ZONE_2', blank=True, null=True)
    status_zone_3 = models.BigIntegerField(db_column='STATUS_ZONE_3', blank=True, null=True)
    status_zone_4 = models.BigIntegerField(db_column='STATUS_ZONE_4', blank=True, null=True)
    stat_brenner = models.BigIntegerField(db_column='STAT_BRENNER', blank=True, null=True)
    stat_z1_r1_br1 = models.BigIntegerField(db_column='STAT_Z1_R1_BR1', blank=True, null=True)
    stat_z1_r1_br2 = models.BigIntegerField(db_column='STAT_Z1_R1_BR2', blank=True, null=True)
    stat_z1_r1_br3 = models.BigIntegerField(db_column='STAT_Z1_R1_BR3', blank=True, null=True)
    stat_z1_r1_br4 = models.BigIntegerField(db_column='STAT_Z1_R1_BR4', blank=True, null=True)
    stat_z1_r1_br5 = models.BigIntegerField(db_column='STAT_Z1_R1_BR5', blank=True, null=True)
    stat_z1_r2_br1 = models.BigIntegerField(db_column='STAT_Z1_R2_BR1', blank=True, null=True)
    stat_z1_r2_br2 = models.BigIntegerField(db_column='STAT_Z1_R2_BR2', blank=True, null=True)
    stat_z1_r2_br3 = models.BigIntegerField(db_column='STAT_Z1_R2_BR3', blank=True, null=True)
    stat_z1_r2_br4 = models.BigIntegerField(db_column='STAT_Z1_R2_BR4', blank=True, null=True)
    stat_z1_r2_br5 = models.BigIntegerField(db_column='STAT_Z1_R2_BR5', blank=True, null=True)
    stat_z1_r3_br1 = models.BigIntegerField(db_column='STAT_Z1_R3_BR1', blank=True, null=True)
    stat_z1_r3_br2 = models.BigIntegerField(db_column='STAT_Z1_R3_BR2', blank=True, null=True)
    stat_z1_r3_br3 = models.BigIntegerField(db_column='STAT_Z1_R3_BR3', blank=True, null=True)
    stat_z1_r3_br4 = models.BigIntegerField(db_column='STAT_Z1_R3_BR4', blank=True, null=True)
    stat_z1_r3_br5 = models.BigIntegerField(db_column='STAT_Z1_R3_BR5', blank=True, null=True)
    stat_z1_r4_br1 = models.BigIntegerField(db_column='STAT_Z1_R4_BR1', blank=True, null=True)
    stat_z1_r4_br2 = models.BigIntegerField(db_column='STAT_Z1_R4_BR2', blank=True, null=True)
    stat_z1_r4_br3 = models.BigIntegerField(db_column='STAT_Z1_R4_BR3', blank=True, null=True)
    stat_z1_r4_br4 = models.BigIntegerField(db_column='STAT_Z1_R4_BR4', blank=True, null=True)
    stat_z1_r4_br5 = models.BigIntegerField(db_column='STAT_Z1_R4_BR5', blank=True, null=True)
    stat_z2_r1_br1 = models.BigIntegerField(db_column='STAT_Z2_R1_BR1', blank=True, null=True)
    stat_z2_r1_br2 = models.BigIntegerField(db_column='STAT_Z2_R1_BR2', blank=True, null=True)
    stat_z2_r1_br3 = models.BigIntegerField(db_column='STAT_Z2_R1_BR3', blank=True, null=True)
    stat_z2_r1_br4 = models.BigIntegerField(db_column='STAT_Z2_R1_BR4', blank=True, null=True)
    stat_z2_r1_br5 = models.BigIntegerField(db_column='STAT_Z2_R1_BR5', blank=True, null=True)
    stat_z2_r2_br1 = models.BigIntegerField(db_column='STAT_Z2_R2_BR1', blank=True, null=True)
    stat_z2_r2_br2 = models.BigIntegerField(db_column='STAT_Z2_R2_BR2', blank=True, null=True)
    stat_z2_r2_br3 = models.BigIntegerField(db_column='STAT_Z2_R2_BR3', blank=True, null=True)
    stat_z2_r2_br4 = models.BigIntegerField(db_column='STAT_Z2_R2_BR4', blank=True, null=True)
    stat_z2_r2_br5 = models.BigIntegerField(db_column='STAT_Z2_R2_BR5', blank=True, null=True)
    stat_z2_r3_br1 = models.BigIntegerField(db_column='STAT_Z2_R3_BR1', blank=True, null=True)
    stat_z2_r3_br2 = models.BigIntegerField(db_column='STAT_Z2_R3_BR2', blank=True, null=True)
    stat_z2_r3_br3 = models.BigIntegerField(db_column='STAT_Z2_R3_BR3', blank=True, null=True)
    stat_z2_r3_br4 = models.BigIntegerField(db_column='STAT_Z2_R3_BR4', blank=True, null=True)
    stat_z2_r3_br5 = models.BigIntegerField(db_column='STAT_Z2_R3_BR5', blank=True, null=True)
    stat_z2_r4_br1 = models.BigIntegerField(db_column='STAT_Z2_R4_BR1', blank=True, null=True)
    stat_z2_r4_br2 = models.BigIntegerField(db_column='STAT_Z2_R4_BR2', blank=True, null=True)
    stat_z2_r4_br3 = models.BigIntegerField(db_column='STAT_Z2_R4_BR3', blank=True, null=True)
    stat_z2_r4_br4 = models.BigIntegerField(db_column='STAT_Z2_R4_BR4', blank=True, null=True)
    stat_z2_r4_br5 = models.BigIntegerField(db_column='STAT_Z2_R4_BR5', blank=True, null=True)
    stat_z3_r1_br1 = models.BigIntegerField(db_column='STAT_Z3_R1_BR1', blank=True, null=True)
    stat_z3_r1_br2 = models.BigIntegerField(db_column='STAT_Z3_R1_BR2', blank=True, null=True)
    stat_z3_r1_br3 = models.BigIntegerField(db_column='STAT_Z3_R1_BR3', blank=True, null=True)
    stat_z3_r1_br4 = models.BigIntegerField(db_column='STAT_Z3_R1_BR4', blank=True, null=True)
    stat_z3_r1_br5 = models.BigIntegerField(db_column='STAT_Z3_R1_BR5', blank=True, null=True)
    stat_z3_r2_br1 = models.BigIntegerField(db_column='STAT_Z3_R2_BR1', blank=True, null=True)
    stat_z3_r2_br2 = models.BigIntegerField(db_column='STAT_Z3_R2_BR2', blank=True, null=True)
    stat_z3_r2_br3 = models.BigIntegerField(db_column='STAT_Z3_R2_BR3', blank=True, null=True)
    stat_z3_r2_br4 = models.BigIntegerField(db_column='STAT_Z3_R2_BR4', blank=True, null=True)
    stat_z3_r2_br5 = models.BigIntegerField(db_column='STAT_Z3_R2_BR5', blank=True, null=True)
    tist_kvz = models.BigIntegerField(db_column='TIST_KVZ', blank=True, null=True)
    tist_zone_1 = models.BigIntegerField(db_column='TIST_ZONE_1', blank=True, null=True)
    tist_zone_2 = models.BigIntegerField(db_column='TIST_ZONE_2', blank=True, null=True)
    tist_zone_3 = models.BigIntegerField(db_column='TIST_ZONE_3', blank=True, null=True)
    tist_zone_4 = models.BigIntegerField(db_column='TIST_ZONE_4', blank=True, null=True)
    tsoll_abgas_kuehl = models.BigIntegerField(db_column='TSOLL_ABGAS_KUEHL', blank=True, null=True)
    tsoll_akt_zone_1 = models.BigIntegerField(db_column='TSOLL_AKT_ZONE_1', blank=True, null=True)
    tsoll_akt_zone_2 = models.BigIntegerField(db_column='TSOLL_AKT_ZONE_2', blank=True, null=True)
    tsoll_akt_zone_3 = models.BigIntegerField(db_column='TSOLL_AKT_ZONE_3', blank=True, null=True)
    tsoll_akt_zone_4 = models.BigIntegerField(db_column='TSOLL_AKT_ZONE_4', blank=True, null=True)
    tsoll_luft_ausblas = models.BigIntegerField(db_column='TSOLL_LUFT_AUSBLAS', blank=True, null=True)
    t_abgas_nach_reku = models.BigIntegerField(db_column='T_ABGAS_NACH_REKU', blank=True, null=True)
    t_abgas_nach_ventilator = models.BigIntegerField(db_column='T_ABGAS_NACH_VENTILATOR', blank=True, null=True)
    t_abgas_regel_kuehlluft = models.BigIntegerField(db_column='T_ABGAS_REGEL_KUEHLLUFT', blank=True, null=True)
    t_abgas_vor_kuehlluft = models.BigIntegerField(db_column='T_ABGAS_VOR_KUEHLLUFT', blank=True, null=True)
    t_luft_nach_reku = models.BigIntegerField(db_column='T_LUFT_NACH_REKU', blank=True, null=True)
    t_luft_vor_reku = models.BigIntegerField(db_column='T_LUFT_VOR_REKU', blank=True, null=True)

    class Meta:
        db_table = 'adjazenzmatrix_variablen'


class beziehungen_variablen(models.Model):
    variablen_index = models.AutoField(primary_key=True)
    variablen = models.CharField(max_length=100, blank=True, null=True)
    beziehung = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'beziehungen_variablen'


class brenner_ofenzone_1(models.Model):
    toi = models.DateTimeField(db_column='TOI', primary_key=True)
    stat_z1_r1_br1 = models.IntegerField(db_column='STAT_Z1_R1_BR1', blank=True, null=True)
    stat_z1_r1_br2 = models.IntegerField(db_column='STAT_Z1_R1_BR2', blank=True, null=True)
    stat_z1_r1_br3 = models.IntegerField(db_column='STAT_Z1_R1_BR3', blank=True, null=True)
    stat_z1_r1_br4 = models.IntegerField(db_column='STAT_Z1_R1_BR4', blank=True, null=True)
    stat_z1_r1_br5 = models.IntegerField(db_column='STAT_Z1_R1_BR5', blank=True, null=True)
    stat_z1_r2_br1 = models.IntegerField(db_column='STAT_Z1_R2_BR1', blank=True, null=True)
    stat_z1_r2_br2 = models.IntegerField(db_column='STAT_Z1_R2_BR2', blank=True, null=True)
    stat_z1_r2_br3 = models.IntegerField(db_column='STAT_Z1_R2_BR3', blank=True, null=True)
    stat_z1_r2_br4 = models.IntegerField(db_column='STAT_Z1_R2_BR4', blank=True, null=True)
    stat_z1_r2_br5 = models.IntegerField(db_column='STAT_Z1_R2_BR5', blank=True, null=True)
    stat_z1_r3_br1 = models.IntegerField(db_column='STAT_Z1_R3_BR1', blank=True, null=True)
    stat_z1_r3_br2 = models.IntegerField(db_column='STAT_Z1_R3_BR2', blank=True, null=True)
    stat_z1_r3_br3 = models.IntegerField(db_column='STAT_Z1_R3_BR3', blank=True, null=True)
    stat_z1_r3_br4 = models.IntegerField(db_column='STAT_Z1_R3_BR4', blank=True, null=True)
    stat_z1_r3_br5 = models.IntegerField(db_column='STAT_Z1_R3_BR5', blank=True, null=True)
    stat_z1_r4_br1 = models.IntegerField(db_column='STAT_Z1_R4_BR1', blank=True, null=True)
    stat_z1_r4_br2 = models.IntegerField(db_column='STAT_Z1_R4_BR2', blank=True, null=True)
    stat_z1_r4_br3 = models.IntegerField(db_column='STAT_Z1_R4_BR3', blank=True, null=True)
    stat_z1_r4_br4 = models.IntegerField(db_column='STAT_Z1_R4_BR4', blank=True, null=True)
    stat_z1_r4_br5 = models.IntegerField(db_column='STAT_Z1_R4_BR5', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'brenner_ofenzone_1'


class brenner_ofenzone_2(models.Model):
    toi = models.DateTimeField(db_column='TOI', primary_key=True)
    stat_z2_r1_br1 = models.IntegerField(db_column='STAT_Z2_R1_BR1', blank=True, null=True)
    stat_z2_r1_br2 = models.IntegerField(db_column='STAT_Z2_R1_BR2', blank=True, null=True)
    stat_z2_r1_br3 = models.IntegerField(db_column='STAT_Z2_R1_BR3', blank=True, null=True)
    stat_z2_r1_br4 = models.IntegerField(db_column='STAT_Z2_R1_BR4', blank=True, null=True)
    stat_z2_r1_br5 = models.IntegerField(db_column='STAT_Z2_R1_BR5', blank=True, null=True)
    stat_z2_r2_br1 = models.IntegerField(db_column='STAT_Z2_R2_BR1', blank=True, null=True)
    stat_z2_r2_br2 = models.IntegerField(db_column='STAT_Z2_R2_BR2', blank=True, null=True)
    stat_z2_r2_br3 = models.IntegerField(db_column='STAT_Z2_R2_BR3', blank=True, null=True)
    stat_z2_r2_br4 = models.IntegerField(db_column='STAT_Z2_R2_BR4', blank=True, null=True)
    stat_z2_r2_br5 = models.IntegerField(db_column='STAT_Z2_R2_BR5', blank=True, null=True)
    stat_z2_r3_br1 = models.IntegerField(db_column='STAT_Z2_R3_BR1', blank=True, null=True)
    stat_z2_r3_br2 = models.IntegerField(db_column='STAT_Z2_R3_BR2', blank=True, null=True)
    stat_z2_r3_br3 = models.IntegerField(db_column='STAT_Z2_R3_BR3', blank=True, null=True)
    stat_z2_r3_br4 = models.IntegerField(db_column='STAT_Z2_R3_BR4', blank=True, null=True)
    stat_z2_r3_br5 = models.IntegerField(db_column='STAT_Z2_R3_BR5', blank=True, null=True)
    stat_z2_r4_br1 = models.IntegerField(db_column='STAT_Z2_R4_BR1', blank=True, null=True)
    stat_z2_r4_br2 = models.IntegerField(db_column='STAT_Z2_R4_BR2', blank=True, null=True)
    stat_z2_r4_br3 = models.IntegerField(db_column='STAT_Z2_R4_BR3', blank=True, null=True)
    stat_z2_r4_br4 = models.IntegerField(db_column='STAT_Z2_R4_BR4', blank=True, null=True)
    stat_z2_r4_br5 = models.IntegerField(db_column='STAT_Z2_R4_BR5', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'brenner_ofenzone_2'


class brenner_ofenzone_3(models.Model):
    toi = models.DateTimeField(db_column='TOI', primary_key=True)
    stat_z3_r1_br1 = models.IntegerField(db_column='STAT_Z3_R1_BR1', blank=True, null=True)
    stat_z3_r1_br2 = models.IntegerField(db_column='STAT_Z3_R1_BR2', blank=True, null=True)
    stat_z3_r1_br3 = models.IntegerField(db_column='STAT_Z3_R1_BR3', blank=True, null=True)
    stat_z3_r1_br4 = models.IntegerField(db_column='STAT_Z3_R1_BR4', blank=True, null=True)
    stat_z3_r1_br5 = models.IntegerField(db_column='STAT_Z3_R1_BR5', blank=True, null=True)
    stat_z3_r2_br1 = models.IntegerField(db_column='STAT_Z3_R2_BR1', blank=True, null=True)
    stat_z3_r2_br2 = models.IntegerField(db_column='STAT_Z3_R2_BR2', blank=True, null=True)
    stat_z3_r2_br3 = models.IntegerField(db_column='STAT_Z3_R2_BR3', blank=True, null=True)
    stat_z3_r2_br4 = models.IntegerField(db_column='STAT_Z3_R2_BR4', blank=True, null=True)
    stat_z3_r2_br5 = models.IntegerField(db_column='STAT_Z3_R2_BR5', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'brenner_ofenzone_3'


class istwerte(models.Model):
    toi = models.DateTimeField(db_column='TOI', primary_key=True)
    zaehler = models.IntegerField(db_column='ZAEHLER', blank=True, null=True)
    tist_zone_1 = models.FloatField(db_column='TIST_ZONE_1', blank=True, null=True)
    tist_zone_2 = models.FloatField(db_column='TIST_ZONE_2', blank=True, null=True)
    tist_zone_3 = models.FloatField(db_column='TIST_ZONE_3', blank=True, null=True)
    tist_zone_4 = models.FloatField(db_column='TIST_ZONE_4', blank=True, null=True)
    tist_kvz = models.FloatField(db_column='TIST_KVZ', blank=True, null=True)
    t_abgas_vor_kuehlluft = models.FloatField(db_column='T_ABGAS_VOR_KUEHLLUFT', blank=True, null=True)
    t_abgas_regel_kuehlluft = models.FloatField(db_column='T_ABGAS_REGEL_KUEHLLUFT', blank=True, null=True)
    t_abgas_nach_reku = models.FloatField(db_column='T_ABGAS_NACH_REKU', blank=True, null=True)
    t_abgas_nach_ventilator = models.FloatField(db_column='T_ABGAS_NACH_VENTILATOR', blank=True, null=True)
    t_luft_vor_reku = models.FloatField(db_column='T_LUFT_VOR_REKU', blank=True, null=True)
    t_luft_nach_reku = models.FloatField(db_column='T_LUFT_NACH_REKU', blank=True, null=True)
    o2_kvz = models.FloatField(db_column='O2_KVZ', blank=True, null=True)
    co_kvz = models.FloatField(db_column='CO_KVZ', blank=True, null=True)
    o2_zone1 = models.FloatField(db_column='O2_ZONE1', blank=True, null=True)
    o2_zone2 = models.FloatField(db_column='O2_ZONE2', blank=True, null=True)
    o2_zone3 = models.FloatField(db_column='O2_ZONE3', blank=True, null=True)
    o2_zone4 = models.FloatField(db_column='O2_ZONE4', blank=True, null=True)
    o2_vor_reku = models.FloatField(db_column='O2_VOR_REKU', blank=True, null=True)
    o2_nach_reku = models.FloatField(db_column='O2_NACH_REKU', blank=True, null=True)
    ofenraumdruck_zone_1 = models.FloatField(db_column='OFENRAUMDRUCK_ZONE_1', blank=True, null=True)
    ofenraumdruck_zone_2 = models.FloatField(db_column='OFENRAUMDRUCK_ZONE_2', blank=True, null=True)
    ofenraumdruck_zone_3 = models.FloatField(db_column='OFENRAUMDRUCK_ZONE_3', blank=True, null=True)
    ofenraumdruck_zone_4 = models.FloatField(db_column='OFENRAUMDRUCK_ZONE_4', blank=True, null=True)
    tsoll_akt_zone_1 = models.FloatField(db_column='TSOLL_AKT_ZONE_1', blank=True, null=True)
    tsoll_akt_zone_2 = models.FloatField(db_column='TSOLL_AKT_ZONE_2', blank=True, null=True)
    tsoll_akt_zone_3 = models.FloatField(db_column='TSOLL_AKT_ZONE_3', blank=True, null=True)
    tsoll_akt_zone_4 = models.FloatField(db_column='TSOLL_AKT_ZONE_4', blank=True, null=True)
    tsoll_luft_ausblas = models.FloatField(db_column='TSOLL_LUFT_AUSBLAS', blank=True, null=True)
    tsoll_abgas_kuehl = models.FloatField(db_column='TSOLL_ABGAS_KUEHL', blank=True, null=True)
    status_zone_1 = models.IntegerField(db_column='STATUS_ZONE_1', blank=True, null=True)
    status_zone_2 = models.IntegerField(db_column='STATUS_ZONE_2', blank=True, null=True)
    status_zone_3 = models.IntegerField(db_column='STATUS_ZONE_3', blank=True, null=True)
    status_zone_4 = models.IntegerField(db_column='STATUS_ZONE_4', blank=True, null=True)
    status_strasse = models.IntegerField(db_column='STATUS_STRASSE', blank=True, null=True)
    f_luft_z1 = models.FloatField(db_column='F_LUFT_Z1', blank=True, null=True)
    f_luft_z2 = models.FloatField(db_column='F_LUFT_Z2', blank=True, null=True)
    f_luft_z3 = models.FloatField(db_column='F_LUFT_Z3', blank=True, null=True)
    f_luft_z4 = models.FloatField(db_column='F_LUFT_Z4', blank=True, null=True)
    f_gas_z1 = models.FloatField(db_column='F_GAS_Z1', blank=True, null=True)
    f_gas_z2 = models.FloatField(db_column='F_GAS_Z2', blank=True, null=True)
    f_gas_z3 = models.FloatField(db_column='F_GAS_Z3', blank=True, null=True)
    f_gas_z4 = models.FloatField(db_column='F_GAS_Z4', blank=True, null=True)
    stat_z1_r1_br1 = models.IntegerField(db_column='STAT_Z1_R1_BR1', blank=True, null=True)
    stat_z1_r1_br2 = models.IntegerField(db_column='STAT_Z1_R1_BR2', blank=True, null=True)
    stat_z1_r1_br3 = models.IntegerField(db_column='STAT_Z1_R1_BR3', blank=True, null=True)
    stat_z1_r1_br4 = models.IntegerField(db_column='STAT_Z1_R1_BR4', blank=True, null=True)
    stat_z1_r1_br5 = models.IntegerField(db_column='STAT_Z1_R1_BR5', blank=True, null=True)
    stat_z1_r2_br1 = models.IntegerField(db_column='STAT_Z1_R2_BR1', blank=True, null=True)
    stat_z1_r2_br2 = models.IntegerField(db_column='STAT_Z1_R2_BR2', blank=True, null=True)
    stat_z1_r2_br3 = models.IntegerField(db_column='STAT_Z1_R2_BR3', blank=True, null=True)
    stat_z1_r2_br4 = models.IntegerField(db_column='STAT_Z1_R2_BR4', blank=True, null=True)
    stat_z1_r2_br5 = models.IntegerField(db_column='STAT_Z1_R2_BR5', blank=True, null=True)
    stat_z1_r3_br1 = models.IntegerField(db_column='STAT_Z1_R3_BR1', blank=True, null=True)
    stat_z1_r3_br2 = models.IntegerField(db_column='STAT_Z1_R3_BR2', blank=True, null=True)
    stat_z1_r3_br3 = models.IntegerField(db_column='STAT_Z1_R3_BR3', blank=True, null=True)
    stat_z1_r3_br4 = models.IntegerField(db_column='STAT_Z1_R3_BR4', blank=True, null=True)
    stat_z1_r3_br5 = models.IntegerField(db_column='STAT_Z1_R3_BR5', blank=True, null=True)
    stat_z1_r4_br1 = models.IntegerField(db_column='STAT_Z1_R4_BR1', blank=True, null=True)
    stat_z1_r4_br2 = models.IntegerField(db_column='STAT_Z1_R4_BR2', blank=True, null=True)
    stat_z1_r4_br3 = models.IntegerField(db_column='STAT_Z1_R4_BR3', blank=True, null=True)
    stat_z1_r4_br4 = models.IntegerField(db_column='STAT_Z1_R4_BR4', blank=True, null=True)
    stat_z1_r4_br5 = models.IntegerField(db_column='STAT_Z1_R4_BR5', blank=True, null=True)
    stat_z2_r1_br1 = models.IntegerField(db_column='STAT_Z2_R1_BR1', blank=True, null=True)
    stat_z2_r1_br2 = models.IntegerField(db_column='STAT_Z2_R1_BR2', blank=True, null=True)
    stat_z2_r1_br3 = models.IntegerField(db_column='STAT_Z2_R1_BR3', blank=True, null=True)
    stat_z2_r1_br4 = models.IntegerField(db_column='STAT_Z2_R1_BR4', blank=True, null=True)
    stat_z2_r1_br5 = models.IntegerField(db_column='STAT_Z2_R1_BR5', blank=True, null=True)
    stat_z2_r2_br1 = models.IntegerField(db_column='STAT_Z2_R2_BR1', blank=True, null=True)
    stat_z2_r2_br2 = models.IntegerField(db_column='STAT_Z2_R2_BR2', blank=True, null=True)
    stat_z2_r2_br3 = models.IntegerField(db_column='STAT_Z2_R2_BR3', blank=True, null=True)
    stat_z2_r2_br4 = models.IntegerField(db_column='STAT_Z2_R2_BR4', blank=True, null=True)
    stat_z2_r2_br5 = models.IntegerField(db_column='STAT_Z2_R2_BR5', blank=True, null=True)
    stat_z2_r3_br1 = models.IntegerField(db_column='STAT_Z2_R3_BR1', blank=True, null=True)
    stat_z2_r3_br2 = models.IntegerField(db_column='STAT_Z2_R3_BR2', blank=True, null=True)
    stat_z2_r3_br3 = models.IntegerField(db_column='STAT_Z2_R3_BR3', blank=True, null=True)
    stat_z2_r3_br4 = models.IntegerField(db_column='STAT_Z2_R3_BR4', blank=True, null=True)
    stat_z2_r3_br5 = models.IntegerField(db_column='STAT_Z2_R3_BR5', blank=True, null=True)
    stat_z2_r4_br1 = models.IntegerField(db_column='STAT_Z2_R4_BR1', blank=True, null=True)
    stat_z2_r4_br2 = models.IntegerField(db_column='STAT_Z2_R4_BR2', blank=True, null=True)
    stat_z2_r4_br3 = models.IntegerField(db_column='STAT_Z2_R4_BR3', blank=True, null=True)
    stat_z2_r4_br4 = models.IntegerField(db_column='STAT_Z2_R4_BR4', blank=True, null=True)
    stat_z2_r4_br5 = models.IntegerField(db_column='STAT_Z2_R4_BR5', blank=True, null=True)
    stat_z3_r1_br1 = models.IntegerField(db_column='STAT_Z3_R1_BR1', blank=True, null=True)
    stat_z3_r1_br2 = models.IntegerField(db_column='STAT_Z3_R1_BR2', blank=True, null=True)
    stat_z3_r1_br3 = models.IntegerField(db_column='STAT_Z3_R1_BR3', blank=True, null=True)
    stat_z3_r1_br4 = models.IntegerField(db_column='STAT_Z3_R1_BR4', blank=True, null=True)
    stat_z3_r1_br5 = models.IntegerField(db_column='STAT_Z3_R1_BR5', blank=True, null=True)
    stat_z3_r2_br1 = models.IntegerField(db_column='STAT_Z3_R2_BR1', blank=True, null=True)
    stat_z3_r2_br2 = models.IntegerField(db_column='STAT_Z3_R2_BR2', blank=True, null=True)
    stat_z3_r2_br3 = models.IntegerField(db_column='STAT_Z3_R2_BR3', blank=True, null=True)
    stat_z3_r2_br4 = models.IntegerField(db_column='STAT_Z3_R2_BR4', blank=True, null=True)
    stat_z3_r2_br5 = models.IntegerField(db_column='STAT_Z3_R2_BR5', blank=True, null=True)
    stat_brenner = models.IntegerField(db_column='STAT_BRENNER', blank=True, null=True)
    bl_eintragetemp = models.FloatField(db_column='BL_EINTRAGETEMP', blank=True, null=True)
    status_betrieb_zone_1 = models.IntegerField(db_column='STATUS_BETRIEB_ZONE_1', blank=True, null=True)
    status_betrieb_zone_2 = models.IntegerField(db_column='STATUS_BETRIEB_ZONE_2', blank=True, null=True)
    status_betrieb_zone_3 = models.IntegerField(db_column='STATUS_BETRIEB_ZONE_3', blank=True, null=True)
    status_betrieb_zone_4 = models.IntegerField(db_column='STATUS_BETRIEB_ZONE_4', blank=True, null=True)

    class Meta:
        db_table = 'istwerte'


class konvektivzone(models.Model):
    toi = models.DateTimeField(db_column='TOI', primary_key=True)
    tist_kvz = models.FloatField(db_column='TIST_KVZ', blank=True, null=True)
    o2_kvz = models.FloatField(db_column='O2_KVZ', blank=True, null=True)
    co_kvz = models.FloatField(db_column='CO_KVZ', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'konvektivzone'


class ofenzone_1(models.Model):
    toi = models.DateTimeField(db_column='TOI', primary_key=True)
    tist_zone_1 = models.FloatField(db_column='TIST_ZONE_1', blank=True, null=True)
    o2_zone1 = models.FloatField(db_column='O2_ZONE1', blank=True, null=True)
    ofenraumdruck_zone_1 = models.FloatField(db_column='OFENRAUMDRUCK_ZONE_1', blank=True, null=True)
    tsoll_akt_zone_1 = models.FloatField(db_column='TSOLL_AKT_ZONE_1', blank=True, null=True)
    status_zone_1 = models.IntegerField(db_column='STATUS_ZONE_1', blank=True, null=True)
    f_luft_z1 = models.FloatField(db_column='F_LUFT_Z1', blank=True, null=True)
    f_gas_z1 = models.FloatField(db_column='F_GAS_Z1', blank=True, null=True)
    status_betrieb_zone_1 = models.IntegerField(db_column='STATUS_BETRIEB_ZONE_1', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ofenzone_1'


class ofenzone_2(models.Model):
    toi = models.DateTimeField(db_column='TOI', primary_key=True)
    tist_zone_2 = models.FloatField(db_column='TIST_ZONE_2', blank=True, null=True)
    o2_zone2 = models.FloatField(db_column='O2_ZONE2', blank=True, null=True)
    ofenraumdruck_zone_2 = models.FloatField(db_column='OFENRAUMDRUCK_ZONE_2', blank=True, null=True)
    tsoll_akt_zone_2 = models.FloatField(db_column='TSOLL_AKT_ZONE_2', blank=True, null=True)
    status_zone_2 = models.IntegerField(db_column='STATUS_ZONE_2', blank=True, null=True)
    f_luft_z2 = models.FloatField(db_column='F_LUFT_Z2', blank=True, null=True)
    f_gas_z2 = models.FloatField(db_column='F_GAS_Z2', blank=True, null=True)
    status_betrieb_zone_2 = models.IntegerField(db_column='STATUS_BETRIEB_ZONE_2', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ofenzone_2'


class ofenzone_3(models.Model):
    toi = models.DateTimeField(db_column='TOI', primary_key=True)
    tist_zone_3 = models.FloatField(db_column='TIST_ZONE_3', blank=True, null=True)
    o2_zone3 = models.FloatField(db_column='O2_ZONE3', blank=True, null=True)
    ofenraumdruck_zone_3 = models.FloatField(db_column='OFENRAUMDRUCK_ZONE_3', blank=True, null=True)
    tsoll_akt_zone_3 = models.FloatField(db_column='TSOLL_AKT_ZONE_3', blank=True, null=True)
    status_zone_3 = models.IntegerField(db_column='STATUS_ZONE_3', blank=True, null=True)
    f_luft_z3 = models.FloatField(db_column='F_LUFT_Z3', blank=True, null=True)
    f_gas_z3 = models.FloatField(db_column='F_GAS_Z3', blank=True, null=True)
    status_betrieb_zone_3 = models.IntegerField(db_column='STATUS_BETRIEB_ZONE_3', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ofenzone_3'


class ofenzone_4(models.Model):
    toi = models.DateTimeField(db_column='TOI', primary_key=True)
    tist_zone_4 = models.FloatField(db_column='TIST_ZONE_4', blank=True, null=True)
    o2_zone4 = models.FloatField(db_column='O2_ZONE4', blank=True, null=True)
    ofenraumdruck_zone_4 = models.FloatField(db_column='OFENRAUMDRUCK_ZONE_4', blank=True, null=True)
    tsoll_akt_zone_4 = models.FloatField(db_column='TSOLL_AKT_ZONE_4', blank=True, null=True)
    status_zone_4 = models.IntegerField(db_column='STATUS_ZONE_4', blank=True, null=True)
    f_luft_z4 = models.FloatField(db_column='F_LUFT_Z4', blank=True, null=True)
    f_gas_z4 = models.FloatField(db_column='F_GAS_Z4', blank=True, null=True)
    status_betrieb_zone_4 = models.IntegerField(db_column='STATUS_BETRIEB_ZONE_4', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ofenzone_4'


class rekuperator(models.Model):
    toi = models.DateTimeField(db_column='TOI', primary_key=True)
    t_abgas_vor_kuehlluft = models.FloatField(db_column='T_ABGAS_VOR_KUEHLLUFT', blank=True, null=True)
    t_abgas_regel_kuehlluft = models.FloatField(db_column='T_ABGAS_REGEL_KUEHLLUFT', blank=True, null=True)
    t_abgas_nach_reku = models.FloatField(db_column='T_ABGAS_NACH_REKU', blank=True, null=True)
    t_luft_vor_reku = models.FloatField(db_column='T_LUFT_VOR_REKU', blank=True, null=True)
    t_luft_nach_reku = models.FloatField(db_column='T_LUFT_NACH_REKU', blank=True, null=True)
    o2_vor_reku = models.FloatField(db_column='O2_VOR_REKU', blank=True, null=True)
    o2_nach_reku = models.FloatField(db_column='O2_NACH_REKU', blank=True, null=True)
    tsoll_luft_ausblas = models.FloatField(db_column='TSOLL_LUFT_AUSBLAS', blank=True, null=True)
    tsoll_abgas_kuehl = models.FloatField(db_column='TSOLL_ABGAS_KUEHL', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rekuperator'


class restwerte(models.Model):
    toi = models.DateTimeField(db_column='TOI', primary_key=True)
    t_abgas_nach_ventilator = models.FloatField(db_column='T_ABGAS_NACH_VENTILATOR', blank=True, null=True)
    status_strasse = models.IntegerField(db_column='STATUS_STRASSE', blank=True, null=True)
    bl_eintragetemp = models.FloatField(db_column='BL_EINTRAGETEMP', blank=True, null=True)
    stat_brenner = models.IntegerField(db_column='STAT_BRENNER', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'restwerte'
