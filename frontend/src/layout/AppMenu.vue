<script setup>
import { ref } from 'vue';

import AppMenuItem from './AppMenuItem.vue';

const model = ref([
    {
        label: 'Pages',
        items: [{ label: 'Users', icon: 'pi pi-fw pi-list', to: '/' }]
    },
    {
        label: 'More',
        items: [
            {
                label: 'View Test Homepage',
                icon: 'pi pi-fw pi-github',
                url: 'https://github.com/tomasrajao/deepersystems-test',
                target: '_blank'
            }
        ]
    }
]);
</script>

<template>
    <ul class="layout-menu">
        <template v-for="(item, i) in model" :key="item">
            <app-menu-item v-if="!item.separator" :item="item" :index="i"></app-menu-item>
            <li v-if="item.separator" class="menu-separator"></li>
        </template>
    </ul>
</template>

<style lang="scss" scoped></style>
