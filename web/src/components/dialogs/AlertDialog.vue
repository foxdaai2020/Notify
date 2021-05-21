<template>
    <v-dialog>
        <v-card>
            <v-card-text>
                <slot name="content" />
            </v-card-text>
            <v-card-actions class="justify-center">
                 <slot name="action" />
            </v-card-actions>
        </v-card>
    </v-dialog>
</template>