<script setup>
import { getUser, createUser, updateUser, deleteUser, getUsersData } from "@/service/UserService";
import { FilterMatchMode } from "@primevue/core/api";
import { useToast } from "primevue/usetoast";
import { onMounted, ref } from "vue";



const toast = useToast();
const dt = ref();
const users = ref();
const userDialog = ref(false);
const deleteUserDialog = ref(false);
const deleteUsersDialog = ref(false);
const user = ref({});
const selectedUsers = ref();
const filters = ref({
  global: { value: null, matchMode: FilterMatchMode.CONTAINS },
});
const submitted = ref(false);
const roles = ref([
  { label: "ADMIN", value: "ADMIN" },
  { label: "MANAGER", value: "MANAGER" },
  { label: "TESTER", value: "TESTER" },
]);

const usersData = async () => {
  try {
    users.value = await getUsersData();
  } catch (error) {
    console.error("Failed to load users", error);
  }
};

onMounted(usersData);

function openNew() {
  user.value = {};
  submitted.value = false;
  userDialog.value = true;
}
function hideDialog() {
  userDialog.value = false;
  submitted.value = false;
}

function editUser(usr) {
  user.value = { ...usr };
  userDialog.value = true;
}

function confirmDeleteUser(usr) {
  user.value = usr;
  deleteUserDialog.value = true;
}

function getStatusLabel(roles) {
  switch (roles) {
    case "ADMIN":
      return "danger";

    case "MANAGER":
      return "info";

    case "TESTER":
      return "success";

    default:
      return null;
  }
}
</script>

<template>
  <div>
    <div class="card">
      <Toolbar class="mb-6">
        <template #start>
          <Button
            label="Create user"
            icon="pi pi-plus"
            severity="secondary"
            class="mr-2"
            @click="openNew"
          />
        </template>
      </Toolbar>

      <DataTable
        ref="dt"
        :value="users"
        dataKey="id"
        :paginator="true"
        :rows="10"
        :filters="filters"
        paginatorTemplate="FirstPageLink PrevPageLink PageLinks NextPageLink LastPageLink CurrentPageReport RowsPerPageDropdown"
        :rowsPerPageOptions="[5, 10, 25]"
        currentPageReportTemplate="Showing {first} to {last} of {totalRecords} users"
      >
        <template #header>
          <div class="flex flex-wrap gap-2 items-center justify-between">
            <h4 class="m-0">User list</h4>
          </div>
        </template>

        <Column
          field="username"
          header="Username"
          sortable
          style="min-width: 12rem"
        ></Column>
        <Column field="role" header="Role" sortable style="min-width: 16rem">
          <template #body="slotProps">
            <Tag
              v-for="role in slotProps.data.roles"
              :value="role.toUpperCase()"
              :severity="getStatusLabel(role.toUpperCase())"
            /> </template
        ></Column>
        <Column header="Timezone" field="preferences" style="min-width: 12rem"></Column>
        <Column header="Is Active?" style="min-width: 8rem">
          <template #body="slotProps">
            <i
              class="pi"
              :class="{
                'pi-check-circle text-green-500 ': slotProps.data.active,
                'pi-times-circle text-red-500': !slotProps.data.active,
              }"
            ></i>
          </template>
        </Column>
        <Column
          field="created_ts"
          header="Last Updated At"
          sortable
          style="min-width: 10rem"
        >
          <template #body="slotProps">
            {{ slotProps.data.created_ts["$date"].toString() }}
          </template>
        </Column>
        <Column field="created_ts" header="Created At" sortable style="min-width: 12rem">
          <template #body="slotProps">
            {{ slotProps.data.created_ts["$date"].toString() }}
          </template>
        </Column>
        <Column header="Actions" :exportable="false" style="min-width: 12rem">
          <template #body="slotProps">
            <Button
              icon="pi pi-pencil"
              outlined
              rounded
              class="mr-2"
              @click="editUser(slotProps.data)"
            />
            <Button
              icon="pi pi-trash"
              outlined
              rounded
              severity="danger"
              @click="confirmDeleteUser(slotProps.data)"
            />
          </template>
        </Column>
      </DataTable>
    </div>

    <Dialog
      v-model:visible="userDialog"
      :style="{ width: '450px' }"
      header="Edit user"
      :modal="true"
    >
      <div class="flex flex-col gap-6">
        <div>
          <label for="username" class="block font-bold mb-3">Username</label>
          <InputText
            id="name"
            v-model="user.username"
            required="true"
            autofocus
            :invalid="submitted && !user.username"
            fluid
          />
          <small v-if="submitted && !user.name" class="text-red-500"
            >Name is required.</small
          >
        </div>
        <div>
          <label for="role" class="block font-bold mb-3">Role</label>
        </div>

      </div>
      <template #footer>
        <Button label="Cancel" icon="pi pi-times" text @click="hideDialog" />
        <Button label="Save" icon="pi pi-check" @click="saveUser" />
      </template>
    </Dialog>

    <Dialog
      v-model:visible="deleteUserDialog"
      :style="{ width: '450px' }"
      header="Confirm"
      :modal="true"
    >
      <div class="flex items-center gap-4">
        <i class="pi pi-exclamation-triangle !text-3xl" />
        <span v-if="user"
          >Are you sure you want to delete <b>{{ user.username }}</b
          >?</span
        >
      </div>
      <template #footer>
        <Button label="No" icon="pi pi-times" text @click="deleteUserDialog = false" />
        <Button label="Yes" icon="pi pi-check" @click="UserService.deleteUser(user._id)" />
      </template>
    </Dialog>

    <Dialog
      v-model:visible="deleteUsersDialog"
      :style="{ width: '450px' }"
      header="Confirm"
      :modal="true"
    >
      <div class="flex items-center gap-4">
        <i class="pi pi-exclamation-triangle !text-3xl" />
        <span v-if="user">Are you sure you want to delete the selected users?</span>
      </div>
      <template #footer>
        <Button label="No" icon="pi pi-times" text @click="deleteUsersDialog = false" />
        <Button label="Yes" icon="pi pi-check" text @click="deleteSelectedUsers" />
      </template>
    </Dialog>
  </div>
</template>
